import math

in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


num_tests = read_int()
tests = []
for n_t in range(num_tests):
    ls = read_int()
    tests.append(ls)

for t in tests:

    def value_fn(n):
        # math.isqrt(x) is accurate and not math.floor(math.sqrt(x))
        return n - math.isqrt(n)


    s, e, st = 1, 2 * t, set()
    while s <= e:
        m = (s + e) // 2
        val = value_fn(m)
        if val >= t:
            st.add(m)
            e = m - 1
        else:
            s = m + 1
    op_fn(min(st))
