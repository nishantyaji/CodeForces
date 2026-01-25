import collections

in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())

def read_str() -> str:
    return in_fn().strip()

t = read_int()
ins = []
for _ in range(t):
    ins.append(read_str())

count = collections.Counter()
res = []
for s in ins:
    if count[s] == 0:
       res.append("OK")
    else:
        res.append(s + str(count[s]))
    count[s] += 1
for r in res:
    op_fn(r)