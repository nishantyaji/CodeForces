# https://codeforces.com/problemset/problem/2014/A

in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


num_tests = read_int()
tests = []
for n_t in range(num_tests):
    [n, k] = read_int_arr()
    a = read_int_arr()
    tests.append([k, a])

for [k, a] in tests:
    stock = 0
    cnt = 0
    for x in a:
        if x >= k:
            stock += x
        else:
            if x == 0 and stock > 0:
                cnt += 1
                stock -= 1
    op_fn(cnt)
