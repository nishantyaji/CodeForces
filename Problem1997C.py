# https://codeforces.com/problemset/problem/1997/C
num_tests = int(input())
test_strs = []
for n_t in range(num_tests):
    str_len = input()
    in_str = input()
    test_strs.append(in_str)


def solve(s: str):
    ls = list(s)
    ls[0] = "("

    for i in range(len(s) - 2, 1, -2):
        if ls[i - 1] == "(":
            ls[i] = ")"
        else:
            ls[i] = "("

    stack, res = [], 0
    for i, c in enumerate(ls):
        if c == "(":
            stack.append(i)
        elif c == ")":
            val = stack.pop()
            res += (i - val)

    print(res)


for s in test_strs:
    solve(s)
