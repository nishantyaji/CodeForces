import collections
import math
import platform

in_fn = input
op_fn = print

input_file = platform.node() and platform.node().startswith("LAPTOP-")
if input_file:
    filename = "Problem1520D.txt"
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
    n = read_int()
    a = read_int_arr()
    tests.append(a)

for t in tests:
    my_dict, res = collections.defaultdict(int), 0
    for i, tx in enumerate(t):
        my_dict[tx - i] += 1
    res = sum([math.comb(v, 2) for k, v in my_dict.items()])
    op_fn(res)
