import sys

in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().split(sep)))


num_tests = read_int()
tests = []
for n_t in range(num_tests):
    [n, k] = read_int_arr()
    lines = []
    for _ in range(n):
        lines.append(read_int_arr())
    tests.append([n, k, lines])

for [n, k, lines] in tests:
    d = dict()
    if k > 1:
        d[k - 1] = 0
    else:
        d[k - 1] = -sys.maxsize
    d[k] = 0
    d[k + 1] = 0

    flag = False
    for [x, y] in lines:
        if [x, y] == [k, k]:
            op_fn("YES")
            flag = True
            break

        if x <= k - 1 and y >= k + 1:
            continue
        elif x <= k - 1 and y == k:
            d[k] += 1
            d[k - 1] += 1
            continue
        elif x == k and y == k:
            d[k] += 1
        if y >= k + 1 and x == k:
            d[k] += 1
            d[k + 1] += 1

    if not flag:
        if d[k] > d[k - 1] and d[k] > d[k + 1]:
            op_fn("YES")
        else:
            op_fn("NO")
