# https://codeforces.com/problemset/problem/2014/C
import math

in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


num_tests = read_int()
tests = []
for n_t in range(num_tests):
    n = read_int()
    a = read_int_arr()
    tests.append(a)

for t in tests:
    if len(t) <= 2:
        op_fn("-1")
        continue

    t.sort()

    lent = len(t)
    idx = math.ceil((lent + 1) / 2) - 1
    val = lent * (2 * t[idx]) - sum(t)
    op_fn(max(0, val + 1))
