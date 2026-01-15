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
    ls = read_int_arr()
    tests.append(ls)

for t in tests:
    mx = max(t)
    is_mx_odd = mx % 2 == 1
    even, odd = 0, 0
    for n in t:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
    if even == 0 or odd == 0:
        op_fn(mx)
    else:
        s = sum(t)
        op_fn(s - (odd - 1))
