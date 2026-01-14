in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


num_tests = read_int()
tests = []
for _ in range(num_tests):
    _ = read_int()
    arr = read_int_arr()
    tests.append(arr)

for t in tests:
    bins = [format(x, "b") for x in t]
    length = max([len(x) for x in bins])
    ones = [0] * length
    for b in bins:
        for i, c in enumerate(b[::-1]):
            ones[i] += (1 if c == "1" else 0)
    zeros = [0] * length
    for i in range(length):
        zeros[i] = len(t) - ones[i]
    mx = -1
    vals = []
    bins = [s.rjust(length, "0") for s in bins]
    for b in bins:
        res = 0
        for i, c in enumerate(b[::-1]):
            if c == "1":
                res += zeros[i] * pow(2, i)
            else:
                res += ones[i] * pow(2, i)
        vals.append(res)
    op_fn(max(vals))
