import sys

in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))

# Can be solved using monotonic stack (from end/right to start/left of the input array)
_ = read_int()
arr = read_int_arr()
arr.reverse()


class SegmentTree:
    def __init__(self, size: int):
        # size = size of compressed map (= 1 + max_elem_of_compressed_map)
        self.size = size
        self.st = [sys.maxsize] * (4 * size)
        self.invalid = sys.maxsize

    def seg_op(self, left: int, right: int) -> int:
        return min([left, right])

    def update(self, place: int, val: int):
        self._update_(0, 0, self.size, place, val)

    def _update_(self, index: int, low: int, high: int, place: int, val: int):
        if low == high:
            if self.st[index] > 1000000000:
                self.st[index] = val
            return
        mid = (low + high) // 2
        if low <= place <= mid:
            self._update_(2 * index + 1, low, mid, place, val)
        else:
            self._update_(2 * index + 2, mid + 1, high, place, val)

        self.st[index] = self.seg_op(self.st[2 * index + 1], self.st[2 * index + 2])

    def query(self, l_query: int, r_query: int):
        return self._query_(0, 0, self.size, l_query, r_query)

    def _query_(self, index: int, low: int, high: int, l_query: int, r_query: int):
        if low >= l_query and high <= r_query:
            return self.st[index]
        if high < l_query or low > r_query:
            return self.invalid
        mid = (low + high) // 2
        low_val = self._query_(2 * index + 1, low, mid, l_query, r_query)
        high_val = self._query_(2 * index + 2, mid + 1, high, l_query, r_query)
        return self.seg_op(low_val, high_val)


co_map = {x: i for i, x in enumerate(sorted(set(arr)))}
st = SegmentTree(len(arr) + 1)
res = []
for index, a in enumerate(arr):
    qr = st.query(0, co_map[a] - 1)
    if qr > 1000000000:
        res.append(-1)
    else:
        res.append(index - qr - 1)
    st.update(co_map[a], index)
res.reverse()
op_fn(" ".join(map(str, res)))
