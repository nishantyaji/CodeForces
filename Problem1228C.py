import math

in_fn = input
op_fn = print


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().split(sep)))


[x, n] = read_int_arr()

limit = math.ceil(math.sqrt(1e9))
primes = [True] * (limit + 1)
limit_sq = math.ceil(math.sqrt(limit))
primes[0], primes[1] = False, False

for i in range(2, limit_sq + 1):
    for j in range(2, limit_sq + 1):
        if i * j <= limit:
            primes[i * j] = False

prime_list = [i for i, a in enumerate(primes) if a]

base = int(1e9 + 7)
factors = []
x_copy = x
for a in prime_list:
    if x_copy % a == 0:
        pw = 0
        while x_copy % a == 0:
            pw += 1
            x_copy //= a
        factors.append((a, pw))
    if x_copy == 1:
        break
if x_copy > 1:
    factors.append((x_copy, 1))

res = 1
for fac, a in factors:
    if fac <= n:
        pw_limit = math.ceil(math.log(n, fac))
        pw_sum = 0
        for i in range(1, pw_limit + 1):
            if pow(fac, i) <= n:
                pw_sum += (n // pow(fac, i))
        res *= pow(fac, pw_sum, base)
        res = res % base

op_fn(res)
