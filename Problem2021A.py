import bisect

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
    t.sort()
    while len(t) > 1:
        avg = (t[0] + t[1]) // 2
        t = t[2:]
        bisect.insort_left(t, avg)
    op_fn(t[0])
