import re

workflows = {}
parts = []
with open('./input.txt') as f:
    for line in f:
        if line.strip() == '':
            break
        m1 = re.match(r'(.*){(.*)}', line)
        rules = []
        for token in m1.group(2).split(','):
            m2 = re.match(r'([xmas])([<>])([0-9]*):(.*)', token)
            if m2 is None:
                rules.append((token, ))
            else: 
                rules.append((m2.group(1), m2.group(2), int(m2.group(3)), m2.group(4)))
        workflows[m1.group(1)] = rules

    for line in f:
        m = re.match(r'{x=(.*),m=(.*),a=(.*),s=(.*)}', line)
        parts.append({'x' : int(m.group(1)), 'm' : int(m.group(2)), 'a' : int(m.group(3)), 's' : int(m.group(4))})

ops = {
    '<' : lambda a, b : a < b,
    '>' : lambda a, b : a > b
}

ans = 0
for part in parts:
    name = 'in'
    while not (name=='A' or name=='R'):
        for rule in workflows[name]:
            if len(rule) == 1:
                name = rule[0]
                break
            category, op, score, nxt = rule
            if ops[op](part[category], score):
                name = nxt
                break
    if name == 'A':
        ans += sum(part[category] for category in 'xmas')
print(ans)