import bisect
import copy

in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


num_tests = read_int()
tests = []
for n_t in range(num_tests):
    [n, q] = read_int_arr()
    a = read_int_arr()
    b = read_int_arr()
    queries = []
    for _ in range(q):
        queries.append(read_int_arr())
    tests.append([a, b, queries])

mod_base = 998244353
for [a, b, queries] in tests:

    new_a = sorted(copy.deepcopy(a))
    new_b = sorted(copy.deepcopy(b))
    temp = 1
    for i in range(len(new_a)):
        this_min = min(new_a[i], new_b[i]) % mod_base
        temp = (temp * this_min) % mod_base
    res = [temp]
    for [op, x] in queries:
        x = x - 1
        if op == 1:
            val = a[x]
            a[x] = val + 1
            r_idx = bisect.bisect_right(new_a, val)
            min_then = min(new_b[r_idx - 1], new_a[r_idx - 1])
            new_a[r_idx - 1] = val + 1
        else:
            val = b[x]
            b[x] = val + 1
            r_idx = bisect.bisect_right(new_b, val)
            min_then = min(new_b[r_idx - 1], new_a[r_idx - 1])
            new_b[r_idx - 1] = val + 1
        min_now = min(new_b[r_idx - 1], new_a[r_idx - 1])
        mul = (min_now * pow(min_then, -1, mod_base)) % mod_base
        temp = (temp * mul) % mod_base
        res.append(temp)
    op_fn(" ".join(list(map(str, res))))
