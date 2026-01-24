in_fn = input
op_fn = print


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


h, t = read_int_arr()

flag = 1
# Simulate
while True:
    if flag:
        if h >= 2 and t >= 2:
            h -= 2
            t -= 2
        elif h == 1 and t >= 12:
            h -= 1
            t -= 12
        elif t >= 22:
            t -= 22
        else:
            op_fn("Hanako")
            break
    else:
        if t >= 22:
            t -= 22
        elif t >= 12 and h >= 1:
            t -= 12
            h -= 1
        elif t >= 2 and h >= 2:
            t -= 2
            h -= 2
        else:
            op_fn("Ciel")
            break
    flag ^= 1
