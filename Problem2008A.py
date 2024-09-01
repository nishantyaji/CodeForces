num_tests = int(input())
tests = []
for n_t in range(num_tests):
    ls = list(map(int, input().split()))
    tests.append(ls)

# tests = [[0,1], [0,3], [2,0], [2,3], [3,1]]

for [a, b] in tests:
    if a == 0:
        if b % 2 == 0:
            print("YES")
            continue
        else:
            print("NO")
            continue
    else:
        a_mod = a % 2
        b_mod = b % 2

        if a_mod == 0 and b_mod == 0:
            print("YES")
            continue
        elif a_mod == 0 and b_mod == 1:
            print("YES")
            continue
        elif a_mod == 1 and b_mod == 0:
            print("NO")
            continue
        elif a_mod == 1 and b_mod == 1:
            print("NO")
            continue
    print("")
