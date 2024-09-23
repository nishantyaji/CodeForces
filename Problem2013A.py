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
    [x, y] = read_int_arr()
    tests.append([n, x, y])

for [n, x, y] in tests:
    if y >= x:
        op_fn(math.ceil(n / x))
    else:
        op_fn(math.ceil(n / y))
