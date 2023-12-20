import collections, math

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


c = 1
record = {'lt':0, 'qh':0, 'bq':0, 'vz':0}
while any(v==0 for v in record.values()):
    q = collections.deque([('unknown', 'broadcaster', 'L')])
    while q:
        pre, cur, puls = q.popleft()
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
            nxt_puls = 'L' if all(memory[cur].values()) else 'H'
            q.extend((cur, nxt, nxt_puls) for nxt in nxts[cur])
            if cur in record and nxt_puls=='H':
                record[cur] = c
    c += 1



lcm = 1
for v in record.values():
    lcm = lcm*v // math.gcd(lcm, v)
print(lcm)