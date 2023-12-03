def solution(a, h, w, x, ys)
  ok = false
  
  ys.product([0, 1, -1], [0, 1, -1]).each do |y, dx, dy|
    i = x+dx
    j = y+dy
    next unless 0<=i && i<h && 0<=j && j<w
    if %w(1 2 3 4 5 6 7 8 9 0 .).none?{|t| a[i][j]==t}
      ok = true
      break
    end
  end

  return 0 if !ok
  ys.map{|y| a[x][y]}.join.to_i
end

A = IO.readlines('input.txt').map(&:strip)
H = A.size
W = A[0].size

ys = []
sum = 0
(0...H).each do |x|
  (0...W).each do |y|
    if A[x][y] =~ /[0-9]/
      ys << y
    else
      if !ys.empty? 
        sum += solution(A, H, W, x, ys)
        ys.clear
      end
    end
  end

  if !ys.empty?
    sum += solution(A, H, W, x, ys)
    ys.clear
  end
end

p sum

