in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().split(sep)))


num_tests = read_int()
tests = []
for n_t in range(num_tests):
    ls = read_int_arr()
    tests.append(ls)

for [n, k] in tests:
    q, r = divmod(k, n - 1)
    if r == 0:
        r = n - 1
        q -= 1
    op_fn(q * n + r)
