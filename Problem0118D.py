import functools

in_fn = input
op_fn = print


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


[n1, n2, k1, k2] = read_int_arr()
base = 100000000
@functools.cache
def dp_fn(x: int, y: int, xk: int, yk: int):
    res = 0
    if x == 0 and y == 0:
        return 1
    if x == 0 and y > 0:
        return 0
    if x > 0 and y == 0:
        if x <= xk:
            return 1
        else:
            return 0

    # Assume 1/x is first
    for i in range(1, min(x, xk) + 1):
        for j in range(1, min(y, yk) + 1):
            res = (res + dp_fn(x - i, y - j, xk, yk)) % base
    return res % base


res = dp_fn(n1, n2, k1, k2) + dp_fn(n2, n1, k2, k1)
op_fn(res % base)
