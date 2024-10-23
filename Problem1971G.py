import collections
import platform

in_fn = input
op_fn = print

input_file = platform.node() and platform.node().startswith("LAPTOP-")
if input_file:
    filename = "Problem1971G.txt"
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
    my_dict = collections.defaultdict(dict)
    for tx in t:
        q, r = divmod(tx, 4)
        # Convert indices to string since they are fast
        # https://codeforces.com/blog/entry/129364?#comment-1192807
        q, r = str(q), str(r)
        if q not in my_dict:
            my_dict[q] = collections.defaultdict(int)
        my_dict[q][r] += 1

    res = []
    for tx in t:
        q, r = divmod(tx, 4)
        q = str(q)
        for i in range(4):
            if not my_dict[q][str(i)] or my_dict[q][str(i)] == 0:
                continue
            res.append(int(q) * 4 + i)
            my_dict[q][str(i)] -= 1
            break

    op_fn(" ".join(list(map(str, res))))