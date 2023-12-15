def to_hash(step: str) -> int:
    hash = 0
    for ch in step:
        hash += ord(ch)
        hash *= 17
        hash %= 256
    return hash


if __name__ == '__main__':
    with open('./input.txt') as f:
        steps = f.readline().strip().split(',')
    ans = sum(map(to_hash, steps))
    print(ans)
    