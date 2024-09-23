# https://codeforces.com/problemset/problem/2014/D

import collections

in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


def read_2d_int_arr(num_rows, sep=" ") -> list[list[int]]:
    return [read_int_arr(sep) for _ in range(num_rows)]


num_tests = read_int()
tests = []
for n_t in range(num_tests):
    [n, d, k] = read_int_arr()
    jobs = read_2d_int_arr(k)
    tests.append([n, d, k, jobs])

for [n, d, k, jobs] in tests:
    add_changes = collections.defaultdict(list)
    remove_changes = collections.defaultdict(list)
    for i, [l, r] in enumerate(jobs):
        add_changes[l].append(i + 1)
        remove_changes[r].append(i + 1)

    num_jobs = []
    st = set()
    for i in range(1, d + 1):
        for a in add_changes[i]:
            st.add(a)

    num_jobs.append(len(st))

    mxval, mxindex, mnval, mnindex = len(st), 0, len(st), 0
    for i in range(d + 1, n + 1):
        for r in remove_changes[i - d]:
            st.remove(r)
        for a in add_changes[i]:
            st.add(a)
        num_jobs.append(len(st))

        if len(st) > mxval:
            mxval = len(st)
            mxindex = i - d
        if len(st) < mnval:
            mnval = len(st)
            mnindex = i - d

    op_fn("%d %d" % (mxindex + 1, mnindex + 1))
