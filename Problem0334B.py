# https://codeforces.com/problemset/problem/334/B
import collections

num_tests = 1
tests = []
for n_t in range(num_tests):
    coords = []
    for i in range(8):
        ls = list(map(int, input().split()))
        coords.append(ls)
    tests.append(coords)

for ps1 in tests:
    ps = [(x[0], x[1]) for x in ps1]
    xc = collections.Counter(list(map(lambda x: x[0], ps)))
    yc = collections.Counter(list(map(lambda x: x[1], ps)))

    x2a = [k for (k, v) in xc.items() if v == 2]
    y2a = [k for (k, v) in yc.items() if v == 2]
    x13a = [k for (k, v) in xc.items() if v == 3]
    y13a = [k for (k, v) in yc.items() if v == 3]

    if len(xc) == 3 and len(yc) == 3 and len(x2a) == 1 and len(y2a) == 1 and len(x13a) == 2 and len(y13a) == 2:
        all_pos = []
        for x_ in xc.keys():
            for y_ in yc.keys():
                all_pos.append((x_, y_))
        temp = set(all_pos)
        temp.remove((x2a[0], y2a[0]))
        if set(ps) == temp and (x13a[0] - x2a[0]) * (x13a[1] - x2a[0]) < 0 and (y13a[0] - y2a[0]) * (
                y13a[1] - y2a[0]) < 0:
            print("respectable")
            continue

    print("ugly")
