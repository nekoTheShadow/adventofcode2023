def f(field)
  n = field.size
  (0..n-2).each do |i|
    return i+1 if [i+1, n-(i+1)].min.times.all?{|j| field[i-j]==field[i+j+1]}
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
