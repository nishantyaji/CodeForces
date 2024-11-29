import math

in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


num_tests = read_int()
tests = []
for n_t in range(num_tests):
    n = read_int()
    tests.append(n)

for n in tests:
    pw = math.floor(math.log2(n))


    def find_ans(n):

        prefix, suffix = [2, 1], []
        if n % 2 == 0:
            for px in range(2, pw + 1):
                suffix.append(2 ** px - 1)
                suffix.append(2 ** px)
            st = set(suffix + prefix)
            return prefix + [i for i in range(1, n + 1) if i not in st] + suffix
        else:
            return find_ans(n - 1) + [n]


    val = 2 ** (pw + 1) - 1 if n % 2 == 0 else n
    op_fn(val)
    op_fn(" ".join(list(map(str, find_ans(n)))))
