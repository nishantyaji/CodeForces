# https://codeforces.com/contest/344/problem/B
in_str = input()
v = list(map(lambda x: int(x), in_str.split()))
x, rx = divmod(v[1] + v[2] - v[0], 2)
y, ry = divmod(v[2] + v[0] - v[1], 2)
z, rz = divmod(v[0] + v[1] - v[2], 2)
if rx + ry + rz > 0 or any(map(lambda m: m < 0, [x, y, z])):
    print("Impossible")
else:
    print("%d %d %d" % (z, x, y))
