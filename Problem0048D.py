import collections
import sys

in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


_ = read_int()
arr = read_int_arr()

count = collections.Counter(arr)
pairs = [(k, v) for  k, v in count.items()]
pairs.sort()
prev = sys.maxsize
impossible = False
mx = pairs[0][1]
if pairs[0][0] != 1:
    impossible = True
else:
    prev_k = 0
    for k, v in pairs:
        if v > prev or k != prev_k + 1:
            impossible = True
            break
        prev = v
        prev_k = k
if impossible:
    op_fn("-1")
else:
    res = []
    for a in arr:
        res.append(count[a])
        count[a] -= 1
    op_fn(mx)
    op_fn(" ".join(map(str, res)))