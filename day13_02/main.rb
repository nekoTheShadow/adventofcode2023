def f(field)
  n = field.size
  (0..n-2).each do |i|
    ok = true
    c = 0
    [i+1, n-(i+1)].min.times do |j|
      a = field[i-j]
      b = field[i+j+1]
      c += (0...a.size).count{|k| a[k]!=b[k]}
      if c > 1
        ok = false
        break
      end
    end
    return i+1 if ok && c==1
  end
  nil
end

fields = []
field = []
IO.foreach('./input.txt', :chomp => true) do |line|
  if line.empty?
    fields << field
    field = []
  else
    field << line.chars
  end
  nil
end
fields << field

sum = 0
fields.each do |field|
  w = f(field)
  if w.nil?
    sum += f(field.transpose)
  else
    sum += w*100
  end
end
p sum
