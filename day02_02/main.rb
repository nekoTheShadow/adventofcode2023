sum = 0
IO.foreach('./input.txt', :chomp => true) do |line|
  h = {'red' => 0, 'blue' => 0, 'green' => 0}
  line[line.index(':')+1..].split(/[;,]/).map{_1.strip.split}.each do |ball, color|
    h[color] = [h[color], ball.to_i].max
  end
  sum += h.values.reduce(1, :*)
end
p sum