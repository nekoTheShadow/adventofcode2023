import re

infos = []
with open('./input.txt') as f:
    for line in f:
        m = re.match(r'(.) (.+) \((.+)\)', line)
        direction = m.group(1)
        size = int(m.group(2))
        color = m.group(3)
        infos.append((direction, size, color))

borders = []
x = 0
y = 0
perimeter = 0
for direction, size, color in infos:
    if direction == 'L': y -= size
    if direction == 'R': y += size
    if direction == 'U': x -= size
    if direction == 'D': x += size
    borders.append((x, y))
    perimeter+=size

area = 0
for i in range(len(borders)-1):
    x1, y1 = borders[i]
    x2, y2 = borders[i+1]
    area += (x1+x2)*(y2-y1)
area = abs(area)//2
print(area-perimeter//2+1 + perimeter)