in_fn = input
op_fn = print

num_tests = int(in_fn())
tests = []
for n_t in range(num_tests):
    ls = list(map(int, in_fn().split()))
    tests.append(ls)

for t in tests:
    op_fn(t[1] - t[0])