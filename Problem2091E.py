import bisect
import functools
import math

in_fn = input
op_fn = print

def read_int() -> int:
    return int(in_fn().strip())


num_tests = read_int()
tests = []
for n_t in range(num_tests):
    ls = read_int()
    tests.append(ls)


@functools.cache
def get_primes():
    limit = 10000001
    flag = [0] * limit
    flag[0] = 1
    flag[1] = 1
    sq_u = math.floor(math.sqrt(limit)) + 1
    for i in range(2, sq_u):
        if flag[i] == 0:
            for j in range(i, 1 + (limit + 1) // i):  # these limits are important
                if i * j < limit:
                    flag[i * j] = 1
    primes = [i for i in range(limit) if flag[i] == 0]
    return primes


for t in tests:
    primes = get_primes()
    res = 0
    for i in range(1, 1 + t//2):
        idx = bisect.bisect_right(primes, t//i)
        res += idx
    op_fn(res)
