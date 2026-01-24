import bisect
import itertools

in_fn = input
op_fn = print


series = []

for n in range(1, 5):
    base = "4"*n + "7"*n
    npr = itertools.permutations(base)
    for p in npr:
        series.append(int("".join(p)))

series += [4444477777]
series.sort()

def read_int() -> int:
    return int(in_fn().strip())

i = read_int()
index = bisect.bisect_left(series, i)
op_fn(series[index])