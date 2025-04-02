in_fn = input
op_fn = print


def read_str() -> str:
    return in_fn().strip()


def read_int() -> int:
    return int(in_fn().strip())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


num_tests = read_int()
tests = []
for n_t in range(num_tests):
    [n, k] = read_int_arr()
    tests.append([n, k])

for [n, k] in tests:
    temp = 0
    if n % 2 == 1 and k % 2 == 1:
        nn = n - k
        q, r = divmod(nn, k - 1)
        temp = q if r == 0 else q + 1
        temp += 1
    elif n % 2 == 0 and k % 2 == 1:
        nn = n - (k - 1)
        q, r = divmod(nn, k - 1)
        temp = q if r == 0 else q + 1
        temp += 1
    elif n % 2 == 1 and k % 2 == 0:
        nn = n - (k - 1)
        q, r = divmod(nn, k)
        temp = q if r == 0 else q + 1
        temp += 1
    else:
        q, r = divmod(n, k)
        temp = q if r == 0 else q + 1
    op_fn(temp)
