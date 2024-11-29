import math

in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


num_tests = read_int()
tests = []
for n_t in range(num_tests):
    _ = read_int()
    arr = read_int_arr()
    tests.append(arr)


def freduce(n: int):
    this_pw = 0
    if n % 2 == 0:
        while n % 2 == 0:
            this_pw += 1
            n = n // 2
    return n, this_pw


mod_base = 1000000007
for arr in tests:

    stack = []
    total = 0
    res = []
    for a in arr:
        x_n, local_cum_2 = freduce(a)
        while stack and math.log2(x_n) + (local_cum_2 + stack[-1][1]) > math.log2(stack[-1][0]) + stack[-1][1]:
            total = (total + stack[-1][0] - stack[-1][0] * pow(2, stack[-1][1], mod_base)) % mod_base
            local_cum_2 += stack[-1][1]
            stack.pop()

        stack.append((x_n, local_cum_2))
        total = (total + x_n * pow(2, local_cum_2, mod_base)) % mod_base
        local_cum_2 = 0
        res.append(total)
    op_fn(" ".join(list(map(str, res))))
