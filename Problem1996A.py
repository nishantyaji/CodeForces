# https://codeforces.com/problemset/problem/1996/A

num_tests = int(input())
tests = []
for n_t in range(num_tests):
    l = int(input())
    tests.append(l)

for t in tests:
    print(t // 4 + (t % 4) // 2)
