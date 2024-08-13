num_tests = int(input())
tests = []
for n_t in range(num_tests):
    l = input()
    tests.append(l)

for t in tests:
    res = "NO"
    if len(t) > 2 and t[:2] == "10":
        suf = int(t[2:])
        if suf > 1 and str(suf) == t[2:]:
            res = "YES"
    print(res)
