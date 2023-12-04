lines = IO.readlines('./input.txt').map(&:strip)
n = lines.size
a = Array.new(n, 1)
lines.each_with_index do |line, i|
  cards1 = line[line.index(':')+1..line.index('|')-1].split.map(&:to_i)
  cards2 = line[line.index('|')+1..].split.map(&:to_i)
  c = cards1.count{|card1| cards2.include?(card1)}
  (0...c).each{|j| a[i+j+1]+=a[i] if i+j+1<n}
end
p a.sum