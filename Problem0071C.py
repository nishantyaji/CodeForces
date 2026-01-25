import math

in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


def get_factors(num: int):
    factors = []
    other_factors = [num]
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            factors.append(i)
            other_factors.append(num // i)
    factors = factors + other_factors[::-1]
    return factors


n = read_int()
factors = get_factors(n)
arr = read_int_arr()
res = "NO"

for f in factors:
    if f == 2:
        continue
    for i in range(n // f):
        good = True
        for j in range(f):
            if arr[i + j * (n // f)] == 0:
                good = False
                break
        if good:
            res = "YES"
            break
    if res == "YES":
        break
op_fn(res)
