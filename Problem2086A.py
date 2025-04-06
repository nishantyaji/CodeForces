in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


num_tests = read_int()
tests = []
for n_t in range(num_tests):
    ls = read_int()
    tests.append(ls)

for t in tests:
    op_fn(2 * t)
