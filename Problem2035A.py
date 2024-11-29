in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


num_tests = read_int()
tests = []
for n_t in range(num_tests):
    [n, m, r, c] = read_int_arr()
    tests.append([n, m, r, c])

for [n, m, r, c] in tests:
    res = (n - r) * (m - 1) + (n * m) - ((r - 1) * m + c)
    op_fn(res)
