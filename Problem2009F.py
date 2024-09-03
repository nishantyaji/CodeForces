import itertools

in_fn = input
op_fn = print

num_tests = int(in_fn())
tests = []
for n_t in range(num_tests):
    [n, q] = list(map(int, in_fn().split()))
    arr = list(map(int, in_fn().split()))
    queries = []
    for _ in range(q):
        queries.append(list(map(int, in_fn().split())))
    tests.append([arr, queries])

for [arr, queries] in tests:
    s = arr + arr
    # precompute the total and length before the query runs
    # otherwise O(n) is lost in the loops for queries
    total = sum(arr)
    lena = len(arr)
    prefix = list(itertools.accumulate(s))


    def sum_(nx: int) -> int:
        if nx == 0:
            return 0
        qq, rr = divmod(nx, lena)
        this_res = qq * total

        ee = ((qq + rr) % lena) + lena - 1
        ss = ee - rr
        return this_res + prefix[ee] - prefix[ss]


    for [l, r] in queries:
        rhs = sum_(r)
        lhs = sum_(l - 1)
        res = rhs - lhs
        op_fn(res)
