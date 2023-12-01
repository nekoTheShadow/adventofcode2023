H = {}
(0..9).each{|i| H[i.to_s] = i}
%w(zero one two three four five six seven eight nine).each_with_index{|w, i| H[w] = i} 

sum = 0
IO.foreach('./input.txt', :chomp => true).each do |line|
  digits = []
  (0...line.size).each do |i|
    H.each{|w, x| digits << x if line[i..].start_with?(w)}
  end
  sum += digits[0]*10+digits[-1]
end
p sum