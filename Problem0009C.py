import bisect
import functools

in_fn = input
op_fn = print


@functools.cache
def get_series():
    series = [1]

    for n in range(2, 1025):
        temp = int(format(n, "b"))
        series.append(temp)
    series.sort()
    return series


series = get_series()


def read_int() -> int:
    return int(in_fn().strip())


n = read_int()
index = bisect.bisect_right(series, n)
op_fn(index)
