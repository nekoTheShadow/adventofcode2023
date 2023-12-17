import heapq

city = []
with open('./input.txt') as f:
    for line in f:
        city.append([int(ch) for ch in line.strip()])
h = len(city)
w = len(city[0])

pq = [(0, 0, 0, 4)]
costs = {(0, 0, 4) : 0}
diff = [(1, 0), (-1, 0), (0, 1), (0, -1)]
while pq:
    c, x, y, i = heapq.heappop(pq)
    if costs[(x, y, i)] < c:
        continue
    for j in range(4):
        if i==j or i//2==j//2:
            continue
        nx = x
        ny = y
        nc = costs[(x, y, i)]
        for k in range(0, 10):
            nx += diff[j][0]
            ny += diff[j][1]
            if not (0<=nx<h and 0<=ny<w):
                break
            nc += city[nx][ny]
            if k >= 3:
                if nc < costs.get((nx, ny, j), float('inf')):
                    costs[(nx, ny, j)] = nc
                    heapq.heappush(pq, (nc, nx, ny, j))

ans = float('inf')
for x, y, i in costs:
    if x==h-1 and y==w-1:
        ans = min(ans, costs[(x, y, i)])
print(ans)


