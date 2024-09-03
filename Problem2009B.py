in_fn = input
op_fn = print

num_tests = int(in_fn())
tests = []
for n_t in range(num_tests):
    l = int(in_fn())
    res = []
    for _ in range(l):
        res.append(in_fn())
    tests.append(res)

for t in tests:
    outp = []
    for row in t[::-1]:
        for i in range(4):
            if row[i] == "#":
                outp.append(str(i + 1))
                break
    op_fn(" ".join(outp))
