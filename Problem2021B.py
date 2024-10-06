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
    [n, x] = read_int_arr()
    a = read_int_arr()
    tests.append([x, a])

for [x, arr] in tests:
    r_dict = collections.defaultdict(int)
    cntr = collections.Counter(arr)
    arr_set = set()
    expected = 0
    visited = set()
    res = -1
    for y in range(0, 200000 + 2):
        i_rem = y % x
        if y in cntr:
            if cntr[y] >= 1:
                r_dict[i_rem] += cntr[y] - 1
                if r_dict[i_rem] == 0:
                    del r_dict[i_rem]
        else:
            if r_dict[i_rem] >= 1:
                r_dict[i_rem] -= 1
                if r_dict[i_rem] == 0:
                    del r_dict[i_rem]
            else:
                res = y
                break
    op_fn(res)
