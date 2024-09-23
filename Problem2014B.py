# https://codeforces.com/problemset/problem/2014/B

in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


num_tests = read_int()
tests = []
for n_t in range(num_tests):
    [n, k] = read_int_arr()
    tests.append([n, k])

dp = [[0 for c in range(4)] for r in range(4)]
for i in range(1, 5):
    for j in range(5, 9):
        sm = 0
        for k in range(i, j + 1):
            sm += k
        sm = sm % 2
        dp[i % 4][j % 4] = sm
for [n, k] in tests:
    if k == 1:
        if n % 2 == 1:
            op_fn("NO")
            continue
        else:
            op_fn("YES")
            continue

    if k == 2:
        op_fn("NO")
        continue

    '''
    if k == n:
        if k % 4 == 1:
            op_fn("NO")
            continue
        else:
            op_fn("YES")
            continue

    start = n - k + 1
    end = n

    if start % 2 == 0:
        start += 1
    if end % 2 == 0:
        end -= 1

    num_odds = 1 + (end - start) // 2

    if num_odds % 2 == 0:
        op_fn("YES")
    else:
        op_fn("NO")
    '''

    op_fn("NO" if dp[(n - k + 1) % 4][n % 4] else "YES")
