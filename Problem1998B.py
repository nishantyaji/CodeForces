num_tests = int(input())
tests = []
for n_t in range(num_tests):
    l = input()
    s = input()
    tests.append(list(map(int, s.split())))

for t in tests:
    def val_(i: int):
        if i == len(t):
            return str(1)
        return str(i + 1)

    # q is not unique
    q = []
    for p in t:
        q.append(val_(p))
    print(" ".join(q))
