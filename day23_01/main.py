import sys
sys.setrecursionlimit(10**9)

with open('./input.txt') as f:
    M = [line.strip() for line in f]
H = len(M)
W = len(M[0])
D = {
    '.' : [(0, 1), (0, -1), (1, 0), (-1, 0)],
    '^' : [(-1, 0)],
    '>' : [(0, 1)],
    'v' : [(1, 0)],
    '<' : [(0, -1)],
}

def dfs(x, y, S):
    if x==H-1 and y==W-2:
        return len(S)
    
    ret = 0
    for dx, dy in D[M[x][y]]:
        nx, ny = x+dx, y+dy
        if not (0<=nx<H and 0<=ny<W):
            continue
        if M[nx][ny]=='#':
            continue
        if (nx, ny) in S:
            continue

        S.add((nx, ny))
        ret = max(ret, dfs(nx, ny, S))
        S.remove((nx, ny))
    return ret

print(dfs(0, 1, set()))
