in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


num_tests = read_int()
tests = []
for n_t in range(num_tests):
    l = read_int()
    ls = read_int_arr()
    tests.append(ls)


def gcd(mm, nn):
    small = mm if mm > nn else nn
    large = mm ^ nn ^ small

    r = 1
    while r > 0:
        q, r = divmod(large, small)
        large = small
        small = r

    return large


for t in tests:
    t.sort()
    x = t[0]
    t = t[1:]
    tx = [tt for tt in t if tt % x == 0]

    res = "No"
    if len(tx) == 0:
        res = "No"
    elif len(tx) == 1:
        res = "Yes" if tx[0] == x else "No"
    else:
        gcd1 = tx[0]
        for tt in tx[1:]:
            gcd1 = gcd(gcd1, tt)
        res = "Yes" if gcd1 == x else "No"
    op_fn(res)
