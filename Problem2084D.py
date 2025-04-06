in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


num_tests = read_int()
tests = []
for n_t in range(num_tests):
    [n, m, k] = read_int_arr()
    tests.append([n, m, k])

for [n, m, k] in tests:
    res = [0] * n
    p = n - m * k
    qq, rr = divmod(n, k)
    if qq == 1:
        for i in range(n):
            res[i] = i % k
    else:
        if p == 1:
            pass
        else:
            x = n // m
            max_rem, max_base = -1, -1
            for i in range(k, x + 1):
                q, r = divmod(n, i)
                if r > 0:
                    if q == m:
                        if r > max_rem:
                            max_rem, max_base = r, i
                    else:
                        if i > max_rem:
                            max_rem, max_base = i, i
                else:
                    # remainder is zero, then
                    # we consider the case where q > m then i would be max_rem
                    # if q == m then not possible since all zeros can be covered
                    if q > m and i > max_rem:
                        max_rem, max_base = i, i

            for i in range(n):
                temp = i % max_base
                res[i] = temp
    res_str = " ".join(list(map(str, res)))
    op_fn(res_str)
