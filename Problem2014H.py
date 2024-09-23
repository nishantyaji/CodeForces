# https://codeforces.com/problemset/problem/2014/H
import itertools
import operator
import random
import sys


class SegmentTree:
    def __init__(self, size: int):
        # size = size of compressed map (= 1 + max_elem_of_compressed_map)
        self.size = size
        self.st = [set()] * (4 * size)
        self.invalid = set()

    def build(self, nums: list[int]):
        self._build_(0, 0, self.size - 1, nums)

    def _build_(self, index: int, low: int, high: int, nums: list[int]):
        if low == high:
            # self.st[index] = nums[low]
            self.st[index] = self.unary_op(self.st[index], nums[low])
            return

        mid = (low + high) // 2
        self._build_(2 * index + 1, low, mid, nums)
        self._build_(2 * index + 2, mid + 1, high, nums)
        self.st[index] = self.seg_op(self.st[2 * index + 1], self.st[2 * index + 2])

    def unary_op(self, existing: set, new: int) -> set:
        return {new}

    def seg_op(self, left: set, right: set) -> set:
        return (left - right).union(right - left)

    def update(self, place: int, val: int):
        self._update_(0, 0, self.size - 1, place, val)

    def _update_(self, index: int, low: int, high: int, place: int, val: int):
        if low == high:
            # use unary_op below
            self.st[index] = {val}
            return
        mid = (low + high) // 2
        if low <= place <= mid:
            self._update_(2 * index + 1, low, mid, place, val)
        else:
            self._update_(2 * index + 2, mid + 1, high, place, val)

        self.st[index] = self.seg_op(self.st[2 * index + 1], self.st[2 * index + 2])

    def query(self, l_query: int, r_query: int):
        return self._query_(0, 0, self.size - 1, l_query, r_query)

    def _query_(self, index: int, low: int, high: int, l_query: int, r_query: int):
        if low >= l_query and high <= r_query:
            return self.st[index]
        if high < l_query or low > r_query:
            return self.invalid
        mid = (low + high) // 2
        low_val = self._query_(2 * index + 1, low, mid, l_query, r_query)
        high_val = self._query_(2 * index + 2, mid + 1, high, l_query, r_query)
        return self.seg_op(low_val, high_val)


in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


def read_2d_int_arr(num_rows, sep=" ") -> list[list[int]]:
    return [read_int_arr(sep) for _ in range(num_rows)]


num_tests = read_int()
tests = []
for n_t in range(num_tests):
    [n, q] = read_int_arr()
    a = read_int_arr()
    queries = read_2d_int_arr(q)
    tests.append([a, queries])

for [a, queries] in tests:
    # Segment tree usage leads to "Memory Limit exceeded"
    # Instead use xor hashing: https://codeforces.com/blog/entry/85900
    # Apparently Mo's algo works too. Got to check.
    '''
    st = SegmentTree(len(a))
    st.build(a)
    for [l, r] in queries:
        op_fn("YES" if len(st.query(l-1, r-1)) == 0 else "NO")
    '''

    rand_dict = {}


    def gen_ran(x: int) -> int:
        rand_dict.setdefault(x, random.randrange(1, sys.maxsize))
        return rand_dict[x]


    rands = [gen_ran(y) for y in a]
    xors = list(itertools.accumulate(rands, operator.xor, initial=0))


    def diff(ll, rr):
        return xors[rr] if ll == 1 else xors[rr] ^ xors[ll - 1]


    for [l, r] in queries:
        op_fn("NO" if diff(l, r) else "YES")
