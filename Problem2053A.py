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

for arr in tests:
    res = False
    for i, a in enumerate(arr):
        if i > 0:
            low, high = (a // 2) + 1, 2 * a - 1
            if low <= arr[i - 1] <= high:
                res = True
                break
    op_fn("YES" if res else "NO")
