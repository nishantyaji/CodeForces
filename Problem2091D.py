in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


num_tests = read_int()
tests = []
for n_t in range(num_tests):
    ls = read_int_arr()
    tests.append(ls)

for [n, m, k] in tests:
    q, r = divmod(k, n)
    if r > 0:
        q += 1


    def check(target: int, v: int) -> bool:
        q1, r1 = divmod(m, v + 1)
        if r1 == v:
            q1 += 1
            r1 = 0
        return q1 * v + r1 >= target


    s, e = 1, m
    st = set()
    while s <= e:
        mid = (s + e) // 2
        if check(q, mid):
            st.add(mid)
            e = mid - 1
        else:
            s = mid + 1
    op_fn(min(st))
