import collections

nxts = collections.defaultdict(list)
ops = {}
parents = collections.defaultdict(list)

with open('./input.txt') as f:
    for line in f:
        src, dst = line.strip().split(' -> ')
        if src=='broadcaster':
            cur = 'broadcaster'
            op = '-'
        else:
            cur = src[1:]
            op = src[0]

        nxts[cur].extend(v.strip() for v in dst.split(','))
        ops[cur] = op
        for nxt in nxts[cur]:
            parents[nxt].append(cur)

memory = {}
for cur in nxts:
    if ops[cur]=='%':
        memory[cur] = False 
    if ops[cur]=='&':
        memory[cur] = {parent : False for parent in parents[cur]}



c = {'H' : 0, 'L' : 0}

for _ in range(1000):
    q = collections.deque([('unknown', 'broadcaster', 'L')])
    while q:
        pre, cur, puls = q.popleft()
        c[puls] += 1

        if cur not in ops:
            continue
        
        if ops[cur]=='-':
            q.extend((cur, nxt, puls) for nxt in nxts[cur])

        if ops[cur]=='%':
            if puls=='H':
                continue
            nxt_puls = 'L' if memory[cur] else 'H'
            q.extend((cur, nxt, nxt_puls) for nxt in nxts[cur])
            memory[cur] = not memory[cur]
        
        if ops[cur]=='&':
            memory[cur][pre] = puls=='H'
            if all(memory[cur].values()):
                q.extend((cur, nxt, 'L') for nxt in nxts[cur])
            else:
                q.extend((cur, nxt, 'H') for nxt in nxts[cur])

print(c, c['L']*c['H'])

# lo = 0
# hi = 0
# for _ in range(1):
#     que = collections.deque([('broadcast', 'low')])
#     while que:
#         cur, puls = que.popleft()
#         if puls=='high':
#             hi += 1
#         else:
#             lo += 1
#         if cur == 'broadcast':
#             que.extend((nxt, 'low') for nxt in broadcasts)
#         else:
#             if cur not in graph:
#                 continue
#             for nxt, op in graph[cur]:
#                 if op=='%':
#                     if puls=='high':
#                         continue
#                     if on_off[cur]:
#                         que.append((nxt, 'low'))
#                         on_off[cur] = False
#                     else:
#                         que.append((nxt, 'high'))
#                         on_off[cur] = True
#                 else:
#                     if puls=='high' and memory[cur]:
#                         que.append((nxt, 'low'))
#                     else:
#                         memory[cur] = False
#                         que.append((nxt, 'high'))
# print(hi*lo)