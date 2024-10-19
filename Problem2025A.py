in_fn = input
op_fn = print


def read_str() -> str:
    return in_fn().strip()


def read_int() -> int:
    return int(in_fn().strip())


num_tests = read_int()
tests = []
for n_t in range(num_tests):
    a = read_str()
    b = read_str()
    tests.append([a, b])

for [a, b] in tests:

    if a.startswith(b) or b.startswith(a):
        op_fn(1 + max(len(a), len(b)))
    else:
        i = 0
        for i in range(0, min(len(a), len(b))):
            if a[i] != b[i]:
                break
        delta = 0 if i == 0 else 1
        res = len(a) + len(b) - i + delta
        op_fn(res)
