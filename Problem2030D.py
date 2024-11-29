import itertools

in_fn = input
op_fn = print


def read_str() -> str:
    return in_fn().strip()


def read_int() -> int:
    return int(in_fn().strip())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


def read_2d_int_arr(num_rows, sep=" ") -> list[list[int]]:
    return [read_int_arr(sep) for _ in range(num_rows)]


num_tests = read_int()
tests = []
for n_t in range(num_tests):
    [n, qq] = read_int_arr()
    p = read_int_arr()
    s = read_str()
    queries = read_2d_int_arr(qq)
    tests.append([p, list(s), queries])

for [p, s, queries] in tests:

    pre_max = list(itertools.accumulate(p, max))
    post_min = list(itertools.accumulate(p[::-1], min))[::-1]

    boundaries = set()
    for i, c in enumerate(s):
        if i > 0 and c == "R" and s[i - 1] == "L":
            if pre_max[i - 1] > post_min[i]:
                boundaries.add(i - 1)

    for [q] in queries:
        if s[q - 1] == "L":
            if q - 2 >= 0 and s[q - 2] == "L":
                if pre_max[q - 2] > post_min[q - 1]:
                    boundaries.add(q - 2)
            boundaries.discard(q - 1)
        if s[q - 1] == "R":
            if s[q] == "R":
                if pre_max[q - 1] > post_min[q]:
                    boundaries.add(q - 1)
            if q - 2 >= 0 and s[q - 2] == "L":
                boundaries.discard(q - 2)
        s[q - 1] = "L" if s[q - 1] == "R" else "R"
        op_fn("NO" if len(boundaries) > 0 else "YES")
