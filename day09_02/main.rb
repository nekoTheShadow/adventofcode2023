sum = 0

IO.foreach('./input.txt', :chomp => true) do |line|
  numbers = line.split.map(&:to_i)
  level = 0
  place_holder = 0
  op = 1
  while numbers.uniq.size > 1
    place_holder += op * numbers[0]
    op *= -1
    
    level += 1
    numbers = (0...numbers.size-1).map{|i| numbers[i+1]-numbers[i]}
    
  end
  place_holder += op*numbers[0]
  sum += place_holder
end

p sum