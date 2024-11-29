in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


num_tests = read_int()
tests = []
for n_t in range(num_tests):
    [n, k] = read_int_arr()
    tests.append([n, k])

for [n, k] in tests:
    if k == n and n == 1:
        op_fn("1")
        op_fn("1")
        continue
    elif k >= n or (k == 1 and n > 1):
        op_fn("-1")
        continue
    prev, nxt, res = k - 1, n - k, []
    if (prev % 2 == 0 and nxt % 2 == 1) or (nxt % 2 == 0 and prev % 2 == 1):
        op_fn("-1")
    else:
        if prev % 2 == 1:
            res.append(1)
            res.append(k)
            res.append(k + 1)
        else:
            res.append(1)
            res.append(k - 1)
            res.append(k)
            res.append(k + 1)
            res.append(k + 2)
        op_fn(len(res))
        op_fn(" ".join(list(map(str, res))))
