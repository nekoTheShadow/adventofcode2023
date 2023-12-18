import re

infos = []
with open('./example.txt') as f:
    for line in f:
        m = re.match(r'(.) (.+) \(#(.+)\)', line)
        direction = m.group(1)
        size = int(m.group(2))
        color = m.group(3)
        infos.append((direction, size, color))

borders = []
x = 0
y = 0
perimeter = 0
for _, _, color in infos:
    size = int(color[:5], 16)
    direction = int(color[5])

    if direction == 2: y -= size
    if direction == 0: y += size
    if direction == 3: x -= size
    if direction == 1: x += size
    borders.append((x, y))
    perimeter+=size

area = 0
for i in range(len(borders)-1):
    x1, y1 = borders[i]
    x2, y2 = borders[i+1]
    area += (x1*y2)-(y1*x2)
area = abs(area)//2
print(area-perimeter//2+1 + perimeter)