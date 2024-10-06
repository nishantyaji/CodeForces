import sys

in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


num_tests = read_int()
tests = []
for n_t in range(num_tests):
    # l = read_str()
    [n, m, q] = read_int_arr()
    a = read_int_arr()
    b = read_int_arr()
    tests.append([a, b])

for [a, b] in tests:
    arr_set = sorted(set(a))
    arr = [-1] + [sys.maxsize] * len(arr_set)
    co_map = {}
    count = 0
    for x in a:
        if x not in co_map:
            count += 1
            co_map[x] = count

    for i, bx in enumerate(b):
        if arr[co_map[bx]] == sys.maxsize:
            arr[co_map[bx]] = i

    prev = -1
    prev_found = True
    success = True
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            success = False
            break

    res = "YA" if success else "TIDAK"
    op_fn(res)
