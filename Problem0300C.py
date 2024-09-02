in_fn = input
op_fn = print

num_tests = 1
tests = []
for n_t in range(num_tests):
    ls = list(map(int, in_fn().split()))
    tests.append(ls)

base = 1000000007
for [a, b, n] in tests:

    # Check https://codeforces.com/blog/entry/72527
    # for modular multiplicative inverse
    def inv_(numm: int, pw: int):
        if pw == 1:
            return numm
        prev = inv_(numm, pw // 2)
        if pw % 2 == 1:
            return (numm * prev * prev) % base
        else:
            return (prev * prev) % base


    def is_good(numm: int):
        numstr = list(str(numm))
        if all(map(lambda x: x in [str(a), str(b)], numstr)):
            return True
        return False


    def is_excel(numm: int):
        if not is_good(numm):
            return False
        return is_good(sum(map(int, list(str(numm)))))


    residues = [1] * (n + 1)
    acc = 1
    for i in range(1, n + 1):
        acc = (acc * i) % base
        residues[i] = acc

    d = b - a
    temp = n * a
    res = 1 if is_good(temp) else 0
    num = residues[n]
    den = 1
    for i in range(1, n + 1):
        temp += d
        if is_good(temp):
            den = residues[i] * residues[n - i]
            res += ((num * inv_(den, base - 2)) % base)
    op_fn(res % base)
