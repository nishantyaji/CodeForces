# https://codeforces.com/contest/1991/problem/B

num_tests = int(input())
tests = []
for n_t in range(num_tests):
    l = input()
    ls = list(map(int, input().split()))
    tests.append(ls)

# tests = [[1], [2, 0], [1, 2, 3], [3, 5, 4, 2], [270667904, 337936906, 270532690, 270615570, 2163474]]

for b in tests:
    done = False
    for j in range(1, len(b) - 1):
        if (b[j - 1] & b[j + 1]) != (b[j - 1] & b[j] & b[j + 1]):
            # When a bit is set in b[j-1] and b[j+1] but not in b[j], then it is impossible
            # Suppose a & b = b[j-1], b & c = b[j], c & d = b[j+1]
            # then (a & b & c & d) == (a & (b&b) & (c&c) &d)
            # == (a&b) & (b&c) & (c&d)
            # the if condition checks for
            # (a & b & c & d)== (a&b) & (b&c) & (c&d)
            print("-1")
            done = True
            break
    if not done:
        a = [None] * (len(b) + 1)
        a[0], a[-1] = b[0], b[-1]
        for j in range(1, len(a) - 1):
            a[j] = b[j] | b[j - 1]

        print(" ".join(list(map(str, a))))
