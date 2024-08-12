# https://codeforces.com/contest/1991/problem/A

num_tests = int(input())
tests = []
for n_t in range(num_tests):
    sz = input()
    ls = list(map(int, input().split()))
    tests.append(ls)

for ls in tests:
    print(max([k for i, k in enumerate(ls) if i % 2 == 0]))
