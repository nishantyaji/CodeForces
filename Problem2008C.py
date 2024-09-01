import math

num_tests = int(input())
tests = []
for n_t in range(num_tests):
    ls = list(map(int, input().split()))
    tests.append(ls)

# tests = [[1, 2], [1, 5], [2, 2], [10, 20], [1, 1000000000], [1, 11]]

for [l, r] in tests:
    if l == r:
        print(1)
        continue
    d = r - l
    if d < 3:
        print(2)
        continue

    n = int((math.sqrt(8 * d + 1) - 1) / 2)
    print(n + 1)
