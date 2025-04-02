import collections

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
    tests.append([n, k, a])

for [n, k, arr] in tests:
    cntr = collections.Counter(arr)
    res = 0
    if k == 1:
        if n == 2:
            res = arr[0] + arr[1]
        else:
            edge_max = max(arr[0], arr[-1])
            mx = max(arr[1: -1])
            if arr[0] > mx and arr[-1] > mx:
                res = arr[0] + arr[-1]
            else:
                res = edge_max + mx
    else:
        arr.sort(reverse=True)
        res = sum(arr[:k + 1])
    op_fn(res)
