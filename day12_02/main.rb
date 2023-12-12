def dp(i, j, record, group, memo)
  return memo[[i, j]] if memo.key?([i, j])
  return memo[[i, j]] = j<group.size ? 0 : 1 if record.size<=i
  return memo[[i, j]] = record[i..].include?('#') ? 0 : 1 if group.size<=j
  return memo[[i, j]] = dp(i+1, j, record, group, memo) if record[i]=='.'

  res = 0
  res += dp(i+1, j, record, group, memo) if record[i]=='?'

  k = i+group[j]-1
  res += dp(k+2, j+1, record, group, memo) if record[i..k].size==group[j] && !record[i..k].include?('.') && (k+1==record.size || record[k+1]!='#')

  memo[[i, j]] = res
end

sum = 0
lines = IO.readlines('./input.txt', :chomp => true)
lines.each do |line|
  tokens = line.split
  record = tokens[0]
  group = tokens[1].split(',').map(&:to_i)
  sum += dp(0, 0, ([record]*5).join('?'), group*5, {})
end
p sum