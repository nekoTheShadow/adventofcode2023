lines = IO.readlines('./input.txt', :chomp => true)
lr = lines[0]
graph = lines[2..].to_h do |line|
  _, from, left, right = *line.match(/(...) = \((...), (...)\)/)
  [from, {"L" => left, "R" => right}]
end

ans = 1
graph.keys.each do |start|
  next unless start.end_with?('A')

  res = 0
  cur = start
  until cur.end_with?('Z')
    cur = graph[cur][lr[res%lr.size]]
    res += 1
  end
  
  ans = ans.lcm(res)
end

p ans