def get_src(table, dst):
    for start_dst, start_src, length in table:
        end_dst = start_dst+length-1
        if start_dst<=dst<=end_dst:
            return start_src+(dst-start_dst)
    return dst


def contains(seeds, seed):
    for i in range(0, len(seeds), 2):
        start_seed = seeds[i]
        length = seeds[i+1]
        if start_seed<=seed<=(start_seed+length-1):
            return True
    return False


tables = []
with open('./input.txt') as f:
    first_line = f.readline().strip()
    seeds = list(map(int, first_line[first_line.index(':')+1:].split()))

    table = None
    for line in f:
        if line[0].isalpha():
            if table is not None:
                tables.append(table)
            table = []
        if line[0].isdigit():
            start_dst, start_src, length = map(int, line.split())
            table.append((start_dst, start_src, length))
    tables.append(table)

location = 0
while True:
    dst = location
    for table in reversed(tables):
        dst = get_src(table, dst)
    if contains(seeds, dst):
        print(location)
        break
    location += 1
    