in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn())


num_tests = read_int()
tests = []
for n_t in range(num_tests):
    tests.append(read_int())

for t in tests:
    q, r = divmod(t, 10)
    op_fn(q + r)
