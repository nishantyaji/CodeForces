import itertools

in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


n = read_int()
arr = read_int_arr()

pref = list(itertools.accumulate(arr))
suff = list(itertools.accumulate(arr[::-1]))[::-1]
res = 0
for i in range(1, n):
    if pref[i - 1] == suff[i]:
        res += 1

op_fn(res)
