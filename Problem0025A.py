in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


_ = read_int()
arr = read_int_arr()
even, odd = 0, 0
for a in arr:
    if a % 2 == 0:
        even += 1
    else:
        odd += 1

res = 0
for i, a in enumerate(arr):
    if odd == 1:
        res += ((i + 1) * (a & 1))
    else:
        res += ((i + 1) * ((a & 1) ^ 1))
op_fn(res)
