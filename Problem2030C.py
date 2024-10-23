in_fn = input
op_fn = print


def read_str() -> str:
    return in_fn().strip()


def read_int() -> int:
    return int(in_fn().strip())


num_tests = read_int()
tests = []
for n_t in range(num_tests):
    n = read_int()
    l = read_str()
    tests.append(l)

for t in tests:
    # Alice wins if edge 1 or more than one continuous 1
    if t[0] == "1" or t[-1] == "1":
        op_fn("YES")
    else:
        prev1 = False
        alice_wins = False
        for i in range(len(t)):
            if t[i] == "1" and prev1:
                alice_wins = True
                break
            prev1 = t[i] == "1"
        res = "YES" if alice_wins else "NO"
        op_fn(res)
