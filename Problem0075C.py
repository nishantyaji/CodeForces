import bisect
import math

in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


[a, b] = read_int_arr()
nq = read_int()
queries = []
for _ in range(nq):
    [l, h] = read_int_arr()
    queries.append([l, h])


def gcd(x, y):
    l, s = (x, y) if x > y else (y, x)
    r = 1
    while r > 0:
        q, r = divmod(l, s)
        l = s
        s = r
    return l


def get_factors(num: int):
    factors = [1]
    other_factors = [num]
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            factors.append(i)
            other_factors.append(num // i)
    factors = factors + other_factors[::-1]
    return factors


g = gcd(a, b)
factors = get_factors(g)

res = []
for [low, high] in queries:
    lidx = bisect.bisect_left(factors, low)
    hidx = bisect.bisect_right(factors, high)
    if lidx == hidx:
        if lidx >= len(factors) or factors[lidx] != low or factors[lidx] == high:
            res.append(-1)
        else:
            res.append(factors[lidx])
    else:
        res.append(factors[hidx - 1])

op_fn("\n".join(map(str, res)))
