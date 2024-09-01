num_tests = int(input())
tests = []
for n_t in range(num_tests):
    n = int(input())
    p = list(map(int, input().split()))
    flag = input()
    tests.append([p, flag])

# tests = [
#     [[1], "0"],
#     [[1, 2, 4, 5, 3], "10101"],
#     [[5, 4, 1, 3, 2], "10011"],
#     [[3, 5, 6, 1, 2, 4], "010000"],
#     [[1, 2, 3, 4, 5, 6], "100110"]
# ]


class UnionFind:
    def __init__(self, n: int, flags: str):
        self.parent = list(range(n))
        self.size = [1] * n
        self.black = [0] * n
        for i, f in enumerate(flags):
            if f == "0":
                self.black[i] = 1

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
            self.black[jrep] += self.black[irep]
        else:
            self.parent[jrep] = irep
            self.size[irep] += self.size[jrep]
            self.black[irep] += self.black[jrep]


for p, flags in tests:
    p = [x - 1 for x in p]
    remain = set(list(range(1, len(p))))
    dsu = UnionFind(len(p), flags)
    pres = 0
    while remain:
        e = pres
        f = p[e]
        if f != e and f in remain:
            dsu.union(e, f)
            remain.remove(f)
            pres = f
        else:
            if remain:
                pres = remain.pop()

    print(" ".join(list(map(lambda x: str(dsu.black[dsu.parent[x]]), range(0, len(p))))))
