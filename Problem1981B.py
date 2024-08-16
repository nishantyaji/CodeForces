# https://codeforces.com/contest/1981/problem/B
import math

num_tests = int(input())
tests = []
for n_t in range(num_tests):
    ls = list(map(int, input().split()))
    tests.append(ls)

# The problem boils down to computing
# or(l....r) l <= r
# where l ... r are consecutive numbers
# tests = [
#     [0, 0],
#     [0, 1],
#     [0, 2],
#     [1, 0],
#     [5, 2],
#     [10, 1],
#     [20, 3],
#     [1145, 14],
#     [19198, 10]
# ]


def same_(a: int, b: int) -> int:
    if int(math.log2(a)) != int(math.log2(b)):
        return 0
    lim = int(math.log2(a))
    idx = lim
    for idx in range(lim, 1, -1):
        aq, ar = divmod(a, 2 ** idx)
        bq, br = divmod(b, 2 ** idx)
        if aq != bq:
            break
        a, b = ar, br

    return lim - idx


for [n, m] in tests:
    if m == 0:
        print(n)
        continue
    if m == 1:
        print(max(1, n - 1) | n | (n + 1))
        continue

    s, e = max(n - m, 1), n + m
    sm = same_(s, e)
    num_digits = max(len(bin(s)[2:]), len(bin(e)[2:]))
    if sm == 0:
        print((2 ** num_digits) - 1)
    else:
        diff = num_digits - sm
        com = int(bin(s)[2:][:sm], 2)
        print(com << diff | (2 ** diff - 1))
