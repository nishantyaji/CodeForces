
in_fn = input
op_fn = print

num_tests = int(in_fn())
tests = []
for n_t in range(num_tests):
    l = int(in_fn())
    ips = []
    for _ in range(l):
        ls = list(map(int, in_fn().split()))
        ips.append(ls)
    tests.append(ips)

for cords in tests:
    xmax = max(list(map(lambda x: x[0], cords)))
    dp = [[False for c in range(2)] for r in range(xmax+1)]

    x1s_count = 0
    x0s_count = 0
    for x, y in cords:
        dp[x][y] = True
        if y == 1:
            x1s_count += 1
        else:
            x0s_count += 1

    res = 0
    for x in range(0, xmax + 1):
        if x < xmax - 1:
            if dp[x][1] and dp[x+1][0] and dp[x+2][1]:
                res += 1
            if dp[x][0] and dp[x+1][1] and dp[x+2][0]:
                res += 1

        if dp[x][0] and dp[x][1]:
            res += (x1s_count - 1 + x0s_count - 1)

    op_fn(res)
