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
    if n == 1 or n == 3:
        op_fn(-1)
        continue
    if n % 2 == 0:
        op_fn("".join(["3"] * (n - 2) + ["66"]))
    else:
        op_fn("".join(["3"] * (n - 5) + ["36366"]))
