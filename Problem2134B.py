in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


num_tests = read_int()
tests = []
for n_t in range(num_tests):
    n, k = read_int_arr()
    a = read_int_arr()
    tests.append([n, k, a])

for [_, k, a] in tests:
    res = []
    if len(a) == 1:
        if a[0] == 1:
            res.append(k + 1)
        else:
            res.append(a[0])
    else:
        if k == 1:
            for b in a:
                c = b + 1 if b % 2 == 1 else b
                res.append(c)
        elif k == 2:
            for b in a:
                q, r = divmod(b, 3)
                if r == 2:
                    c = b + 4
                elif r == 1:
                    c = b + 2
                else:
                    c = b
                res.append(c)
        else:
            for b in a:
                q, r = divmod(b, k - 1)
                c = (b + (k - 1 - r) * k) if r > 0 else b
                res.append(c)

    resstr = " ".join(map(str, res))
    op_fn(resstr)
