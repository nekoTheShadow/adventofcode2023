import collections, itertools

with open('./input.txt') as f:
    M = [line.strip() for line in f]
H = len(M)
W = len(M[0])

# G[(x, y)] = {(nx, ny, length), ...}
G = collections.defaultdict(set) 
for x, y in itertools.product(range(H), range(W)):
    if M[x][y]=='#':
        continue
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x+dx, y+dy
        if (0<=nx<H and 0<=ny<W) and M[nx][ny]!='#':
            G[(x, y)].add((nx, ny, 1))

has_next = True
while has_next:
    has_next = False
    for cur, nxts in G.items():
        if len(nxts) != 2:
            continue
        (nx1, ny1, nl1), (nx2, ny2, nl2) = nxts
        G[(nx1, ny1)] = set((x, y, l) for x, y, l in G[(nx1, ny1)] if (x, y) != cur)
        G[(nx1, ny1)].add((nx2, ny2, nl1+nl2))
        G[(nx2, ny2)] = set((x, y, l) for x, y, l in G[(nx2, ny2)] if (x, y) != cur)
        G[(nx2, ny2)].add((nx1, ny1, nl1+nl2))
        del G[cur]
        has_next = True
        break


S = set()
T = 0
U = 0
def dfs(x, y):
    global T, U
    if x==H-1 and y==W-2:
        U = max(T, U)
        return

    for nx, ny, l in G[(x, y)]:
        if (nx, ny) in S:
            continue
        S.add((nx, ny))
        T += l
        dfs(nx, ny)
        S.remove((nx, ny))
        T -= l



dfs(0, 1)
print(U)

