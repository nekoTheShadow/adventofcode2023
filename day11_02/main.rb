U = IO.readlines('./input.txt', :chomp => true).map(&:chars)
H = U.size
W = U[0].size
X = []
Y = []
S = []

(0...H).each do |i|
  X << i if U[i].all?{|c| c=='.'}
end
(0...W).each do |j|
  Y << j if (0...H).all?{|i| U[i][j]=='.'}
end
(0...H).each do |i|
  (0...W).each do |j|
    S << [i, j] if U[i][j] == '#'
  end
end


sum = 0
S.combination(2) do |(x1, y1), (x2, y2)|
  d = (x1-x2).abs+(y1-y2).abs
  d += X.count{|x| [x1,x2].min<=x && x<=[x1,x2].max} * (1000000-1)
  d += Y.count{|y| [y1,y2].min<=y && y<=[y1,y2].max} * (1000000-1)
  sum += d
end
p sum
