import sys
from collections import deque

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
    a = read_int_arr()
    tests.append([k, a])

for [k, a] in tests:
    a.sort()
    a += [sys.maxsize]
    res, prev, sm, dq = -1, a[0], 0, deque()
    for ax in a:
        if ax > prev + 1:
            res = max(res, sm)
            dq = deque()
            dq.append([ax, 1])
            sm = 1
        elif ax == prev + 1 and len(dq) == k:
            # drop first elem
            if len(dq) > 0:
                first, occ = dq.popleft()
                res = max(res, sm)
                sm -= occ
            dq.append([ax, 1])
            sm += 1
        else:
            if len(dq) == 0 or (dq and dq[-1][0] != ax):
                dq.append([ax, 1])
            else:
                dq[-1][1] += 1
            sm += 1
        prev = ax
    res = max(res, sm)
    op_fn(res)
