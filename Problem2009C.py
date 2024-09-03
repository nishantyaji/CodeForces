in_fn = input
op_fn = print

num_tests = int(in_fn())
tests = []
for n_t in range(num_tests):
    ls = list(map(int, in_fn().split()))
    tests.append(ls)

for [x, y, k] in tests:
    xq, xr = divmod(x, k)
    if xr > 0:
        xq += 1
    yq, yr = divmod(y, k)
    if yr > 0:
        yq += 1

    if xq > yq:
        res = 2 * xq - 1
    else:
        res = 2 * yq
    op_fn(res)
