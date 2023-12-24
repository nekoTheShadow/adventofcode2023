import sympy

data = []
with open('input.txt') as f:
    for line in f:
        a, d = line.strip().split('@')
        ax, ay, az = map(int, a.split(','))
        dx, dy, dz = map(int, d.split(','))
        data.append((ax, ay, az, dx, dy, dz))

x1 = sympy.var('x1')
y1 = sympy.var('y1')
z1 = sympy.var('z1')
dx1 = sympy.var('dx1')
dy1 = sympy.var('dy1')
dz1 = sympy.var('dz1')
eq = []
for i, (x2, y2, z2, dx2, dy2, dz2) in enumerate(data):
    exec(f"t{i} = sympy.var('t{i}')")
    eq.append(sympy.Eq(eval(f'x1 + t{i} * dx1'), eval(f'x2 + t{i} * dx2')))
    eq.append(sympy.Eq(eval(f'y1 + t{i} * dy1'), eval(f'y2 + t{i} * dy2')))
    eq.append(sympy.Eq(eval(f'z1 + t{i} * dz1'), eval(f'z2 + t{i} * dz2')))
    if len(eq) > 9:
        break
ans = sympy.solve(eq)[0]
print(ans[x1]+ans[y1]+ans[z1])




# L={20}0000000000000
# U=400000000000000
# ret = 0
# for i in range(len(data)):
#     for j in range(i+1, len(data)):
#         ax1, ay1, az1, dx1, dy1, dz1 = data[i]
#         ax2, ay2, az2, dx2, dy2, dz2 = data[j]

#         # y = A1*x + B1
#         # y = A2*x + B2
#         A1 = dy1/dx1
#         B1 = (ay1*dx1 - ax1*dy1) / dx1
#         A2 = dy2/dx2
#         B2 = (ay2*dx2 - ax2*dy2) / dx2
        
#         # 2つの線分が並行
#         if A1-A2==0:
#             continue

#         # 2つの線分の交点を求める
#         X = (B2-B1) / (A1-A2)
#         Y = A1*X+B1

#         # 交点がいつぶつかるのかを求める
#         T1 = (X-ax1)/dx1
#         T2 = (X-ax2)/dx2
#         if T1>0 and T2>0 and L<=X<=U and L<=Y<=U:
#             ret += 1
# print(ret)