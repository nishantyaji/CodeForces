import collections

in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


num_tests = read_int()
tests = []
for n_t in range(num_tests):
    n = read_int()
    p = read_int_arr()
    d = read_int_arr()
    tests.append([n, p, d])


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, i: int):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int):
        irep = self.find(i)
        jrep = self.find(j)
        if irep == jrep:
            return

        isize = self.size[irep]
        jsize = self.size[jrep]
        if isize < jsize:
            self.parent[irep] = jrep
            self.size[jrep] += self.size[irep]
        else:
            self.parent[jrep] = irep
            self.size[irep] += self.size[jrep]


for [n, p, d] in tests:
    par = {}
    uf = UnionFind(n)
    for i, numm in enumerate(p):
        par[numm] = i + 1
        uf.union(numm - 1, i)

    cntr = collections.Counter()
    find_res = {}
    for i in range(n):
        temp = uf.find(i)
        find_res[i] = temp
        cntr[temp] += 1

    visited = set()

    res = [0] * n
    pref = 0
    for i in range(n):
        irep = find_res[d[i] - 1]
        if irep not in visited:
            pref += uf.size[irep]
            visited.add(irep)
        else:
            pref = res[i - 1]
        res[i] = pref

    res_str = " ".join(list(map(str, res)))
    op_fn(res_str)
