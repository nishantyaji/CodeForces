in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


num_pairs = read_int()
n = read_int_arr()
k = read_int_arr()
tests = list(zip(n, k))

base = 1000000007

for (n, k) in tests:
    if k == n or k == 0:
        op_fn(1)
    else:
        op_fn(pow(2, k, base))
