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
    ls = read_int_arr()
    tests.append(ls)

for t in tests:
    ones = sum(t)
    mn = 1 if ones % 2 == 1 else 0
    mx = ones if ones <= len(t) // 2 else len(t) - ones
    op_fn("%d %d" % (mn, mx))
