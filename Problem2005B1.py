in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


num_tests = read_int()
tests = []
for n_t in range(num_tests):
    [n, m, q] = read_int_arr()
    b = read_int_arr()
    pos = read_int()
    tests.append([n, m, b, pos])

for [n, m, b, pos] in tests:
    b.sort()
    if pos in b:
        ans = 0
    elif pos < b[0]:
        ans = b[0] - 1
    elif pos > b[1]:
        ans = n - b[1]
    else:
        arr = [pos - b[0], b[1] - pos]
        arr.sort()
        small_diff, large_diff = arr[0], arr[1]
        ans = 0
        # The following block can be trimmed, for sure
        if small_diff % 2 == 0:
            if large_diff % 2 == 1:
                ans += (large_diff - (small_diff + 1)) // 2
            else:
                ans += (large_diff - small_diff) // 2
            ans += small_diff
        else:
            if large_diff % 2 == 1:
                ans += (large_diff - small_diff) // 2
            else:
                ans += (large_diff - (small_diff + 1)) // 2
            ans += small_diff
    op_fn(ans)
