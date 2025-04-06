in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


num_tests = read_int()
tests = []
for n_t in range(num_tests):
    l = read_int()
    a = read_int_arr()
    b = read_int_arr()
    tests.append([l, a, b])

for [n, a, b] in tests:
    d = {}
    res = True
    eq_count, eq_index = 0, -1
    for i in range(n):
        if a[i] == b[i]:
            eq_count += 1
            eq_index = i
            continue
        if b[i] in d:
            if d[b[i]] != a[i]:
                res = False
                break
        else:
            d[a[i]] = b[i]

    if eq_count > 1 or (n % 2 == 0 and eq_count > 0) or not res:
        op_fn("-1")
    else:
        b_dict = {x: i for i, x in enumerate(b)}
        a_dict = {x: i for i, x in enumerate(a)}
        out_of_sort = 0
        pairs = []

        if eq_count == 1:
            mid = n // 2
            if eq_index != mid:
                out_of_sort += 1

                pairs.append((eq_index + 1, mid + 1))

                pre_a, pre_b = a[mid], b[mid]
                b_dict[a[eq_index]] = mid
                a_dict[a[eq_index]] = mid
                b_dict[b[mid]] = eq_index
                a_dict[a[mid]] = eq_index

                b[mid] = a[eq_index]
                a[mid] = a[eq_index]
                b[eq_index] = pre_b
                a[eq_index] = pre_a

        for i in range(n - 1):
            if b_dict[a[i]] != n - 1 - i:
                out_of_sort += 1
                pre_x = a_dict[b[n - 1 - i]]
                pre_a = a[pre_x]
                pre_b = b[pre_x]

                a_dict[a[i]] = pre_x
                b_dict[b[i]] = pre_x
                a_dict[a[pre_x]] = i
                b_dict[b[pre_x]] = i

                a[pre_x] = a[i]
                b[pre_x] = b[i]
                a[i] = pre_a
                b[i] = pre_b

                pairs.append((i + 1, pre_x + 1))
        op_fn(out_of_sort)
        for pa in pairs:
            op_fn(str(pa[0]) + " " + str(pa[1]))
