platform = IO.readlines('input.txt', :chomp => true).map(&:chars)
h = platform.size
w = platform[0].size
(0...w).each do |y|
  (0...h).each do |x|
    next if platform[x][y] != 'O'
    
    i = x
    while i > 0
      break if platform[i-1][y]!='.'
      platform[i-1][y], platform[i][y] = platform[i][y], platform[i-1][y]
      i -= 1
    end
  end
end

sum = 0
platform.reverse.each_with_index do |row, i|
  sum += (i+1) * row.count('O')
end
p sum