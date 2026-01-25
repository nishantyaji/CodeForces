import functools
import math

in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


n = read_int()


@functools.cache
def get_primes():
    limit = 1000001
    primes = []
    flag = [0] * limit
    flag[0] = 1
    flag[1] = 1
    for i in range(2, 1 + math.isqrt(limit)):
        if flag[i] == 0:
            for j in range(2, 1 + limit // i):
                if i * j < limit:
                    flag[i * j] = 1
    primes = [i for i, x in enumerate(flag) if x == 0]
    return primes


primes = get_primes()
res = [n]
for p in primes:
    while n % p == 0:
        n = n // p
        res.append(n)
    if n == 1:
        break
op_fn(" ".join(map(str, res)))
