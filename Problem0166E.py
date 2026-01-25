import functools

in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


@functools.cache
def dp_fn(x: int):
    if x <= 2:
        return 0
    elif x == 3:
        return 3
    elif x == 4:
        return 9
    else:
        res = 3 * pow(2, x - 3)
        for i in range(1, x - 3):
            res += (3 * pow(2, i - 1)) * dp_fn(x - 1 - i)
        return res


n = read_int()
n += 1
op_fn(dp_fn(n))