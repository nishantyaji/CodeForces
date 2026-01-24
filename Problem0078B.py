in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


n = read_int()
q, r = divmod(n - 7, 4)
if q > 0:
    res = "VIBGYOR" + "VIBG" * q + "YOR"[:r]
else:
    res = "VIBGYOR" + "GYORVIB"[:r]
op_fn(res)
