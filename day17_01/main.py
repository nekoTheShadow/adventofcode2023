import heapq, collections

city = []
with open('./input.txt') as f:
    for line in f:
        city.append([int(ch) for ch in line.strip()])
h = len(city)
w = len(city[0])

pq = []
heapq.heappush(pq, (0, -1, -1, 0, 0, 0))
score = collections.defaultdict(lambda : float('inf'))
score[(-1, -1, 0, 0, 0)] = 0
while pq:
    cost, pre_x, pre_y, cur_x, cur_y, count = heapq.heappop(pq)
    if score[(pre_x, pre_y, cur_x, cur_y, count)] < cost:
        continue

    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nxt_x, nxt_y = cur_x+dx, cur_y+dy
        if not (0<=nxt_x<h and 0<=nxt_y<w):
            continue
        if nxt_x==pre_x and nxt_y==pre_y:
            continue

        if cur_x-pre_x==dx and cur_y-pre_y==dy:
            if count<3:
                cur_key = (pre_x, pre_y, cur_x, cur_y, count)
                nxt_key = (cur_x, cur_y, nxt_x, nxt_y, count+1)
                if score[cur_key]+city[nxt_x][nxt_y] < score[nxt_key]:
                    score[nxt_key] = score[cur_key]+city[nxt_x][nxt_y]
                    heapq.heappush(pq, (score[nxt_key], *nxt_key))
        else:
            cur_key = (pre_x, pre_y, cur_x, cur_y, count)
            nxt_key = (cur_x, cur_y, nxt_x, nxt_y, 1)
            if score[cur_key]+city[nxt_x][nxt_y] < score[nxt_key]:
                score[nxt_key] = score[cur_key]+city[nxt_x][nxt_y]
                heapq.heappush(pq, (score[nxt_key], *nxt_key))

ans = float('inf')
for (pre_x, pre_y, cur_x, cur_y, count), v in score.items():
    if cur_x==h-1 and cur_y==w-1:
        ans = min(ans, v)
print(ans)