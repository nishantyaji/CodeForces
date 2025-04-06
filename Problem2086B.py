import bisect

in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


num_tests = read_int()
tests = []
for n_t in range(num_tests):
    [n, k, x] = read_int_arr()
    a = read_int_arr()
    tests.append([n, k, x, a])

for [n, k, x, a] in tests:
    sum_a = sum(a)
    if x > sum_a * k:
        op_fn(0)
    elif x == sum_a * k:
        op_fn(1)
    else:
        if min(a) >= x:
            op_fn(k * n)
            continue

        res = 0
        q, r = divmod((sum_a * k) - x, sum_a)
        res += (q * n)

        rem_q = k - q - 1
        to_add = rem_q * sum_a
        rem_x = x - to_add

        pref, prev = [0] * n, 0
        for i in range(0, n):
            pref[i] = prev + a[n - 1 - i]
            prev = pref[i]

        idx = bisect.bisect_left(pref, rem_x)
        res += (n - idx)
        op_fn(res)
