in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


num_tests = read_int()
tests = []
for n_t in range(num_tests):
    n = read_int()
    tests.append(n)

for n in tests:
    res_z = (n - 1)
    res = ["0"] * res_z + ["1"] * (n - res_z)
    res = "".join(res)
    op_fn(res)
