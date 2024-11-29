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
    _ = read_int()
    ls = read_int_arr()
    tests.append(ls)

for a in tests:
    a.sort()
    mx = -1
    for i, ax in enumerate(a):
        if i == len(a) - 2:
            break
        sm = a[i + 1] + ax
        idx = bisect.bisect_left(a, sm)
        mx = max(mx, idx - i)
    op_fn(len(a) - mx)
