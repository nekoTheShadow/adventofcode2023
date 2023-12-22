import re, collections

def dropped_brick(tallest, brick):
    peak = 0
    for x in range(brick[0], brick[3] + 1):
         for y in range(brick[1], brick[4] + 1):
            peak = max(peak, tallest[(x, y)])
    dz = max(brick[2] - peak - 1, 0)
    return (brick[0], brick[1], brick[2] - dz, brick[3], brick[4], brick[5] - dz)

def drop1(tower):
    tallest = collections.defaultdict(int)
    new_tower = []
    for brick in tower:
        new_brick = dropped_brick(tallest, brick)
        new_tower.append(new_brick)
        for x in range(brick[0], brick[3] + 1):
            for y in range(brick[1], brick[4] + 1):
                tallest[(x, y)] = new_brick[5]
    return new_tower

def drop2(tower):
    tallest = collections.defaultdict(int)
    falls = 0
    for brick in tower:
        new_brick = dropped_brick(tallest, brick)
        if brick[2] != new_brick[2]:
            falls += 1
        for x in range(brick[0], brick[3] + 1):
            for y in range(brick[1], brick[4] + 1):
                tallest[(x, y)] = new_brick[5]
    return falls


tower = []
with open('./input.txt') as f:
    for line in f:
        tower.append(list(map(int, re.findall(r'[0-9]+', line))))
tower.sort(key=lambda brick : brick[2])
tower = drop1(tower)

ret = 0
for i in range(len(tower)):
    ret += drop2(tower[:i]+tower[i+1:])
print(ret) 