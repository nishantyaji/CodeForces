import collections
import itertools

in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


num_tests = read_int()
tests = []
for n_t in range(num_tests):
    n = read_int()
    ranges = []
    for _ in range(n):
        ranges.append(read_int_arr())
    tests.append(ranges)

for ranges in tests:
    n = len(ranges)
    if n == 1:
        op_fn("1")
        continue
    singles = {}
    set_single = set()
    dp = collections.defaultdict(int)
    max_pos = -1
    for i, [l, u] in enumerate(ranges):
        if l == u:
            if l not in singles:
                singles[l] = 0
            singles[l] += 1
            dp[l] += 1
            set_single.add(i)
        max_pos = max(max_pos, u)

    cum = [0] * (max_pos + 1)
    for i in range(1, max_pos + 1):
        if dp[i] > 0:
            cum[i] = 1
    prefix = list(itertools.accumulate(cum))
    res = []
    for i, [l, u] in enumerate(ranges):
        if i in set_single:
            res.append("0" if singles[u] > 1 else "1")
        else:
            window = prefix[u] - prefix[l - 1]
            res.append("0" if window == (u - l + 1) else "1")

    op_fn("".join(res))
