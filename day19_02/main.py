import re, collections

def negate(rules):
    new_rules = []
    for rule in rules:
        category = rule[0]
        op = rule[1]
        score = int(rule[2:])
        if op == '<':
            new_rules.append(f'{category}>{score-1}')
        else:
            new_rules.append(f'{category}<{score+1}')
    return new_rules

def dfs(cur, H):
    if cur == 'in':
        return calc(H)
    ret = 0
    for nxt, rules in G[cur]:
        H.append(rules)
        ret += dfs(nxt, H)
        H.pop()
    return ret

def calc(H):
    part = {'x':[0, 4001],'m':[0, 4001],'a':[0, 4001],'s':[0, 4001]}
    for rules in H:
        for rule in rules:
            category = rule[0]
            op = rule[1]
            score = int(rule[2:])
            if op == '<':
                part[category][1] = min(part[category][1], score)
            else:
                part[category][0] = max(part[category][0], score)
    ret = 1
    for category in 'xmas':
        ret *= part[category][1]-part[category][0]-1
    return ret 

lines = []
with open('./input.txt') as f:
    for line in f:
        if line.strip() == '':
            break
        lines.append(line.strip())

G = collections.defaultdict(list)
for line in lines:
    m1 = re.match(r'(.*){(.*)}', line)
    rules = []
    parent = m1.group(1)
    for token in m1.group(2).split(','):
        m2 = re.match(r'([xmas][<>][0-9]*):(.*)', token)
        if m2 is None:
            G[token].append((parent, negate(rules)))
        else:
            rule = m2.group(1)
            child = m2.group(2)
            G[child].append((parent, [*negate(rules), rule]))
            rules.append(rule)

print(dfs('A', []))