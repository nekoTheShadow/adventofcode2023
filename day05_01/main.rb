
def get_dst(map, src)
  map.each do |start_dst, start_src, length|
    end_src = start_src + length - 1
    return start_dst + (src-start_src) if start_src<=src && src<=end_src
  end
  src
end

seeds = []
maps = []

File.open('./input.txt') do |file|
  first_line = file.gets.chomp
  seeds.concat(first_line[first_line.index(':')+1..].split.map(&:to_i))

  map = []
  file.each(:chomp => true) do |line|
    next if line.empty?

    if line =~ /(.*)-to-(.*) map:/
      maps << map if !map.empty?
      map = []
    else
      map << line.split.map(&:to_i)
    end
  end

  maps << map
end

locations = []
seeds.each do |seed|
  dst = seed
  maps.each{|map| dst = get_dst(map, dst)}
  locations << dst
end

p locations.min