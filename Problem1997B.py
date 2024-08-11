# https://codeforces.com/problemset/problem/1997/B

num_tests = int(input())
tests = []
for n_t in range(num_tests):
    l = input()
    s = [input(), input()]
    tests.append(s)

# tests = [[".......x", ".x.xx..."], ["..", ".."], ["xxx", "xxx"], ["..x.x.x.x", "x.......x"]]

for t in tests:
    res = 0
    for i in range(1, len(t[0]) - 1):
        for j in range(0, 2):
            if (t[j][i] == "." and t[j][i - 1] == "." and t[j][i + 1] == "." and t[j ^ 1][i] == "."
                    and t[j ^ 1][i - 1] == "x" and t[j ^ 1][i + 1] == "x"):
                res += 1
    print(res)
