import itertools

with open('./input.txt') as f:
    M = [line.strip() for line in f]
H = len(M)
W = len(M[0])

sx, sy = -1, -1
for x, y in itertools.product(range(H), range(W)):
    if M[x][y]=='S':
        sx, sy = x, y


curs = set()
curs.add((sx, sy))
for _ in range(64):
    nxts = set()
    for x, y in curs:
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx, ny = x+dx, y+dy
            if 0<=nx<H and 0<=ny<W and M[nx][ny]!='#':
                nxts.add((nx, ny))
    curs = nxts

print(len(curs))