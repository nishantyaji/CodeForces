import math

num_tests = int(input())
tests = []
for n_t in range(num_tests):
    l = int(input())
    s = input()
    tests.append(s)

# tests = ["11", "1111", "111101111", "111111111", "111110011111", "1111110001100011000111111"]


def is_square(num_: int) -> bool:
    sqrt_ = int(math.sqrt(num_))
    return sqrt_ * sqrt_ == num_


def giv_ch(num: int, idx: int):
    r = int(math.sqrt(num))
    x, y = divmod(idx, r)

    if x == 0 or x == r - 1:
        return "1"
    else:
        if y == 0 or y == r - 1:
            return "1"
        else:
            return "0"


for t in tests:
    n = len(t)

    if not is_square(n):
        print("No")
        continue

    done = False
    for i, c in enumerate(t):
        if c != giv_ch(n, i):
            done = True
            break

    if done:
        print("No")
    else:
        print("Yes")
