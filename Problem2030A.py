in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


num_tests = read_int()
tests = []
for n_t in range(num_tests):
    l = read_int()
    a = read_int_arr()
    tests.append(a)

for t in tests:
    mx, mn = max(t), min(t)
    op_fn((len(t) - 1) * (mx - mn))
