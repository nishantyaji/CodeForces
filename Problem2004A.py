num_tests = int(input())
tests = []
for n_t in range(num_tests):
    l = int(input())
    ls = list(map(int, input().split()))
    tests.append(ls)

for t in tests:
    if len(t) == 2 and abs(t[0] - t[1]) >= 2:
        print("YES")
        continue
    print("NO")
