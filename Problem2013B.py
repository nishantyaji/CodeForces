# https://codeforces.com/problemset/problem/2013/B

import functools
import operator

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
    if len(t) == 2:
        op_fn(t[1] - t[0])
    elif len(t) == 3:
        op_fn(t[2] - t[1] + t[0])
    else:
        op_fn(t[-1] - (t[-2] - functools.reduce(operator.add, t[:-2])))
