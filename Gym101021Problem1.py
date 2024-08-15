# https://codeforces.com/gym/101021/problem/1

from sys import stdout

s, e, last_eq = 1, 1000000, 1

while s <= e:
    # <= search because s = mid + 1 and e = mid - 1 and there is no == check
    # use binary search
    mid = (s + e) // 2
    print(mid)
    stdout.flush()
    ret = input()
    if ret == ">=":
        last_eq = mid
        s = mid + 1
    else:
        e = mid - 1

print("!", last_eq)
