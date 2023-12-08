lines = IO.readlines('./input.txt', :chomp => true)
lr = lines[0]
graph = lines[2..].to_h do |line|
  _, from, left, right = *line.match(/(...) = \((...), (...)\)/)
  [from, {"L" => left, "R" => right}]
end

cur = "AAA"
i = 0
c = 0
until cur == "ZZZ"
  cur = graph[cur][lr[i]]
  i = (i+1)%lr.size
  c += 1
end
p c
