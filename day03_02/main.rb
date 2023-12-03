def get_gear_no(a, h, w, x, ys)
  ok = false
  
  ys.product([0, 1, -1], [0, 1, -1]).each do |y, dx, dy|
    i = x+dx
    j = y+dy
    next unless 0<=i && i<h && 0<=j && j<w
    return [i, j] if a[i][j]=='*'
  end

  [-1, -1]
end

A = IO.readlines('input.txt').map(&:strip)
H = A.size
W = A[0].size

ys = []
d = Hash.new{|h, k| h[k] = []}
(0...H).each do |x|
  (0...W).each do |y|
    if A[x][y] =~ /[0-9]/
      ys << y
    else
      if !ys.empty? 
        d[get_gear_no(A, H, W, x, ys)] << ys.map{A[x][_1]}.join.to_i
        ys.clear
      end
    end
  end

  if !ys.empty?
    d[get_gear_no(A, H, W, x, ys)] << ys.map{A[x][_1]}.join.to_i
    ys.clear
  end
end

p d.sum{|k, v| v.size==2 ? v[0]*v[1] : 0}

