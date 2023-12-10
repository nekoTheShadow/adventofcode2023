require 'set'

direction = {
  'S' => [[1, 0]],
  '|' => [[-1, 0], [1, 0]],  # north and south
  '-' => [[0, 1], [0, -1]],  # east and west
  'L' => [[-1, 0], [0, 1]],  # north and east
  'J' => [[-1, 0], [0, -1]], # north and west
  '7' => [[1, 0], [0, -1]],  # south and west
  'F' => [[1, 0], [0, 1]],   # south and east
}

maze = IO.readlines('./input.txt', :chomp => true)
h = maze.size
w = maze[0].size
sx, sy = [*0...h].product([*0...w]).find{|i, j| maze[i][j] == 'S'}


stack = [[sx, sy]]
cycle = Set.new
while !stack.empty?
  x, y = stack.pop
  cycle << [x, y]
  direction[maze[x][y]].each do |dx, dy|
    nx = x+dx
    ny = y+dy
    stack << [nx, ny] if !cycle.include?([nx, ny])
  end
end

sum = 0
(0...h).each do |x|
  inside = false
  (0...w).each do |y|
    if cycle.include?([x, y])
      inside = !inside if 'S|F7'.include?(maze[x][y])
    else
      sum += 1 if inside
    end
  end
end

p sum

