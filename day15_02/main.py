def to_hash(step: str) -> int:
    hash = 0
    for ch in step:
        hash += ord(ch)
        hash *= 17
        hash %= 256
    return hash


if __name__ == '__main__':
    import collections

    with open('./input.txt') as f:
        steps = f.readline().strip().split(',')
    boxs = [collections.OrderedDict() for _ in range(256)]
    for step in steps:
        if step.endswith('-'):
            label = step[:-1]
            hash = to_hash(label)
            if label in boxs[hash]:
                del boxs[hash][label]
        else:
            x = step.index('=')
            label = step[:x]
            length = int(step[x+1:])
            boxs[to_hash(label)][label] = length

    ans = 0
    for i, box in enumerate(boxs):
        for j, label in enumerate(box):
            ans += (i+1) * (j+1) * box[label]
    print(ans)