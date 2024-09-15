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
    q, r = divmod(t, 5)
    res = []
    for ch in "aeiou":
        temp = [ch] * q
        if r > 0:
            temp = temp + [ch]
            r -= 1
        res = res + temp
    op_fn("".join(res))
