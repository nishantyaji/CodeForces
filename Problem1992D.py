# https://codeforces.com/contest/1992/problem/D

num_tests = int(input())
tests = []
for n_t in range(num_tests):
    [l, j, f] = list(map(int, input().split()))
    s = input()
    tests.append([l, j, f, s])

# tests = [
#     [6, 2, 0, "LWLLLW"],
#     [6, 1, 1, "LWLLLL"],
#     [6, 1, 1, "LWLLWL"],
#     [6, 2, 15, "LWLLCC"],
#     [6, 10, 0, "CCCCCC"],
#     [6, 6, 1, "WCCCCW"],
# ]

for [n, j, f, s] in tests:
    s = "L" + s + "L"
    dp = [0] * (n + 2)
    w_trav = 0


    def mark(pres: int):
        las = -1
        if s[pres] == "L":
            # if the present cell is land
            # then mark all non-C cells within j (jump max) as possible
            for i in range(1, j + 1):
                if pres + i > n + 1:
                    dp[n + 1] = 1
                    return n + 1
                if s[pres + i] == "L":
                    las = pres + i
                    dp[pres + i] = 1
        return las


    last, loop = 0, True
    while loop:
        temp_l = last
        while temp_l != -1 and last < n + 1:
            temp_l = mark(last)
            if temp_l > -1:
                last = temp_l
        if dp[n + 1] == 1:
            print("YES")
            loop = False
            continue
        else:
            temp = - 1
            for i in range(j, -1, -1):
                if s[last + i] == "W":
                    temp = last + i
                    break
            if temp == -1:
                print("NO")
                loop = False
                continue

            i = 1
            w_trav += 1
            while w_trav <= f and s[temp + i] == "W":
                i += 1
                w_trav += 1
            if s[temp + i] == "C" or w_trav > f:
                print("NO")
                loop = False
                continue
            if s[temp + i] == "L":
                dp[temp + i] = 1
                last = temp + i
