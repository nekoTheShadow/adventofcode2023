def move(platform, d, dx, dy)
  h = platform.size
  w = platform[0].size

  iter_x = (d==:N || d==:W) ? (0...h).each : (0...h).reverse_each
  iter_y = (d==:N || d==:W) ? (0...w).each : (0...w).reverse_each 

  iter_x.each do |x|
    iter_y.each do |y|
      next if platform[x][y] != 'O'
      
      i, j = x, y
      while 0<=i+dx && i+dx<h && 0<=j+dy && j+dy<w
        break if platform[i+dx][j+dy]!='.'
        platform[i+dx][j+dy], platform[i][j] = platform[i][j], platform[i+dx][j+dy]
        i += dx
        j += dy
      end
    end
  end
end

platform = IO.readlines('input.txt', :chomp => true).map(&:chars)
diffs = [[:N, -1, 0], [:W, 0, -1], [:S, 1, 0], [:E, 0, 1]]
visited = {}
visited[platform.map(&:dup)] = 0

(0..).each do |i|
  d, dx, dy = diffs[i%4]
  move(platform, d, dx, dy)
  break if visited.key?(platform)
  visited[platform.map(&:dup)] = i+1
end

s = visited[platform]
e = visited.values.max

target, _ = visited.find{|k, v| v == s + (4000000000-s) % (e-s+1)}
p target.reverse.each_with_index.sum{|row, i| (i+1)*row.count('O')}
