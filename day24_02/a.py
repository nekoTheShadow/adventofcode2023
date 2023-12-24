from sympy import var, Eq, solve

particles = []

sx = var("sx")
sy = var("sy")
sz = var("sz")

vx = var("vx")
vy = var("vy")
vz = var("vz")

eq = []

for l in open("input.txt"):
    p = l.split(" @ ")
    ps = list(map(int, p[0].split(", ")))
    vs = list(map(int, p[1].split(", ")))

    particles.append((ps, vs))

    ts = "t{}".format(len(eq) // 3)
    exec(f'{ts} = var("{ts}")')

    eq.append(Eq(eval(f"sx + vx * {ts}"), eval(f"ps[0] + vs[0] * {ts}")))
    eq.append(Eq(eval(f"sy + vy * {ts}"), eval(f"ps[1] + vs[1] * {ts}")))
    eq.append(Eq(eval(f"sz + vz * {ts}"), eval(f"ps[2] + vs[2] * {ts}")))

    # 3 pos, 3 vs + 3 ts minimum length, otherwise same solution with more calcaution
    if len(eq) > 9:
        break

print(eq)
ans = solve(eq)[0]
print(ans[sx] + ans[sy] + ans[sz])