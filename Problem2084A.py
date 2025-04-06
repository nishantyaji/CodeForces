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
    if t % 2 == 0:
        op_fn(-1)
    else:
        res = [t, 2, 1]
        for i in range(3, t):
            res.append(i)
        res_str = " ".join(list(map(str, res)))
        op_fn(res_str)
