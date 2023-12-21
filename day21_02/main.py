import itertools

T = 26501365

with open('./input.txt') as f:
    M = [line.strip() for line in f]
N = len(M)

sx, sy = -1, -1
for x, y in itertools.product(range(N), range(N)):
    if M[x][y]=='S':
        sx, sy = x, y


curs = set()
curs.add((sx, sy))
c = 1
p = []
while len(p) < 3: 
    nxts = set()
    for x, y in curs:
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx, ny = x+dx, y+dy
            if M[nx%N][ny%N]!='#':
                nxts.add((nx, ny))
    curs = nxts
    if c%N==T%N:
        p.append(len(nxts))
    c += 1

p0 = p[0]
p1 = p[1]-p[0]
p2 = p[2]-p[1]
ans = p0 + (p1*(T//N)) + ((T//N)*((T//N)-1)/2)*(p2-p1)
print(ans)
