import collections

in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


def read_2d_int_arr(num_rows, sep=" ") -> list[list[int]]:
    return [read_int_arr(sep) for _ in range(num_rows)]


num_tests = read_int()
tests = []
for n_t in range(num_tests):
    [n, m] = read_int_arr()
    matrix = read_2d_int_arr(n)
    tests.append([n, m, matrix])

for [n, m, matrix] in tests:
    mx = -1

    for i in range(n):
        for j in range(m):
            mx = max(mx, matrix[i][j])

    row_cnt, col_cnt = collections.Counter(), collections.Counter()
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == mx:
                row_cnt[i] += 1
                col_cnt[j] += 1

    row_mx, col_mx = max(row_cnt.values()), max(col_cnt.values())
    row, col = -1, -1
    if row_mx > col_mx:
        for r in range(n):
            if row_cnt[r] == row_mx:
                row = r

        col_set = set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == mx:
                    if i != row:
                        col_set.add(j)

        if len(col_set) > 1:
            op_fn(mx)
        else:
            op_fn(mx - 1)

    else:
        for c in range(m):
            if col_cnt[c] == col_mx:
                col = c

        row_set = set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == mx:
                    if j != col:
                        row_set.add(i)

        if len(row_set) > 1:
            op_fn(mx)
        else:
            op_fn(mx - 1)
