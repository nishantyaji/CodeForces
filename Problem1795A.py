import platform

in_fn = input
op_fn = print

input_file = platform.node() and platform.node().startswith("LAPTOP-")
if input_file:
    filename = "Problem1795A.txt"
    f = open(filename, "r")
    in_fn = f.readline


    def check_file(args):
        exp = f.readline().strip()
        if str(args) == exp:
            print("Pass")
        else:
            print("Fail. Expected:", exp, "Got", args)


    op_fn = check_file


def read_str() -> str:
    return in_fn().strip()


def read_int() -> int:
    return int(in_fn().strip())


def read_str_arr(sep=" ") -> list[str]:
    return in_fn().split(sep)


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().split(sep)))


num_tests = read_int()
tests = []
for n_t in range(num_tests):
    ls = read_int_arr()
    s1 = read_str()
    s2 = read_str()
    tests.append([s1, s2])

for [s1, s2] in tests:
    s = s1 + s2[::-1]
    cnt, flag = 0, False
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            cnt += 1
            if cnt > 1:
                op_fn("NO")
                flag = True
                break
    if not flag:
        op_fn("YES")