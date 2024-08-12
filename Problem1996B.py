# https://codeforces.com/contest/1996/problem/B

num_tests = int(input())
tests = []
for n_t in range(num_tests):
    [sz, k] = list(map(int, input().split()))
    # parse
    grid = []
    for i in range(sz):
        grid.append(input())
    tests.append([k, grid])

for k, grid in tests:
    n = len(grid)
    q = n // k
    res = []
    for i in range(q):
        s = ""
        for j in range(q):
            val = grid[i * k][j * k]
            s += val
        res.append(s)
    for r in res:
        print(r)
