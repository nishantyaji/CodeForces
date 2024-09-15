import bisect

in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


def find_ans(pos, arr):
    if pos in arr:
        ans = 0
    elif pos < arr[0]:
        ans = arr[0] - 1
    elif len(arr) > 1 and pos > arr[1]:
        ans = n - arr[1]
    elif len(arr) == 1 and pos > arr[0]:
        ans = n - arr[0]
    else:
        temp_arr = [pos - arr[0], arr[1] - pos]
        temp_arr.sort()
        small_diff, large_diff = temp_arr[0], temp_arr[1]
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
    return ans


num_tests = read_int()
tests = []
for n_t in range(num_tests):
    [n, m, q] = read_int_arr()
    b = read_int_arr()
    queries = read_int_arr()
    tests.append([n, m, b, queries])

for [n, m, b, queries] in tests:
    b.sort()
    for pos1 in queries:
        idx = bisect.bisect_left(b, pos1)
        if idx == 0:
            op_fn(find_ans(pos1, [b[0]]))
        elif idx == len(b):
            op_fn(find_ans(pos1, [b[-1]]))
        else:
            op_fn(find_ans(pos1, [b[idx - 1], b[idx]]))
