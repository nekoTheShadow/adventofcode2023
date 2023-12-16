import sys
sys.setrecursionlimit(10**8)

A = []
with open('./input.txt') as f:
    for line in f:
        A.append(line.strip())
H = len(A)
W = len(A[0])
D = {
    'R' : ( 0,  1),
    'L' : ( 0, -1),
    'U' : (-1,  0),
    'D' : ( 1,  0)
}
NXT = {}
NXT[('R', '/')] = ['U']
NXT[('R', '\\')] = ['D']
NXT[('R', '|')] = ['U', 'D']
NXT[('L', '/')] = ['D']
NXT[('L', '\\')] = ['U']
NXT[('L', '|')] = ['U', 'D']
NXT[('D', '/')] = ['L']
NXT[('D', '\\')] = ['R']
NXT[('D', '-')] = ['L', 'R']
NXT[('U', '/')] = ['R']
NXT[('U', '\\')] = ['L']
NXT[('U', '-')] = ['L', 'R']
MEMO = {}

def dfs(x, y, d):
    if not (0<=x<H and 0<=y<W):
        return 
    if (x, y, d) in MEMO:
        return
    MEMO[(x, y, d)] = True

    if (d, A[x][y]) in NXT:
        for nd in NXT[(d, A[x][y])]:
            dx, dy = D[nd]
            dfs(x+dx, y+dy, nd)
    else:
        dx, dy = D[d]
        dfs(x+dx, y+dy, d)


dfs(0, 0, 'R')
c = {}
for x, y, d in MEMO:
    c[(x, y)] = True
print(len(c))