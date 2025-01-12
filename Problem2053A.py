import platform

in_fn = input
op_fn = print

input_file = platform.node() and platform.node().startswith("LAPTOP-")
if input_file:
    filename = "contest/Problem2053/Problem2053A.txt"
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
    return in_fn().strip().split(sep)


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


def read_2d_int_arr(num_rows, sep=" ") -> list[list[int]]:
    return [read_int_arr(sep) for _ in range(num_rows)]


def read_2d_str_arr(num_rows, sep=" ") -> list[list[str]]:
    return [read_str_arr(sep) for _ in range(num_rows)]


num_tests = read_int()
tests = []
for n_t in range(num_tests):
    # l = read_str()
    n = read_int()
    ls = read_int_arr()
    tests.append(ls)

for arr in tests:
    res = False
    for i, a in enumerate(arr):
        if i > 0:
            low, high = (a // 2) + 1, 2 * a - 1
            if low <= arr[i-1] <= high:
                res = True
                break
    op_fn("YES" if res else "NO")
