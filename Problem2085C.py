import math

in_fn = input
op_fn = print


def read_str() -> str:
    return in_fn().strip()


def read_int() -> int:
    return int(in_fn().strip())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


num_tests = read_int()
tests = []
for n_t in range(num_tests):
    [a, b] = read_int_arr()
    tests.append([a, b])

for x, y in tests:
    mx, mn = max(x, y), min(x, y)
    digits = math.ceil(math.log2(mx))
    if x == y:
        op_fn(-1)
    else:
        res = 2 ** (digits + 1) - mx
        op_fn(res)
