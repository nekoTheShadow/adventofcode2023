def dfs(field, pattern, cur)

  if field.size == cur
    new_pattern = []
    c = 0
    (0...field.size).each do |i|
      if field[i] == '.'
        new_pattern << c if c > 0
        c = 0
      else
        c += 1
      end
    end
    new_pattern << c if c > 0

    return new_pattern == pattern ? 1 : 0
  end
  
  if field[cur] != '?'
    return dfs(field, pattern, cur+1)
  end

  sum = 0
  field[cur] = '#'
  sum += dfs(field, pattern, cur+1)
  field[cur] = '?'

  field[cur] = '.'
  sum += dfs(field, pattern, cur+1)
  field[cur] = '?'

  return sum
end

sum = 0
lines = IO.readlines('./input.txt', :chomp => true)
lines.each do |line|
  tokens = line.split
  field = tokens[0]
  pattern = tokens[1].split(',').map(&:to_i)
  sum += dfs(field, pattern, 0)
end
p sum