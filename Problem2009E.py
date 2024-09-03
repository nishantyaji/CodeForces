import functools

in_fn = input
op_fn = print

num_tests = int(in_fn())
tests = []
for n_t in range(num_tests):
    ls = list(map(int, in_fn().split()))
    tests.append(ls)


@functools.cache
def val_(kk: int, mm: int, nn: int):
    # [k....mm-1][mm....k + n - 1]
    ii = mm - kk
    lhs = kk * ii + (ii * (ii - 1)) // 2
    rhs = (nn - ii) * (kk + ii) + ((nn - ii - 1) * (nn - ii)) // 2
    return lhs - rhs


for [n, k] in tests:
    if n == 2:
        op_fn(1)
        continue
    s, e = k, k + n - 1
    d = {}

    res = -1
    flag = False
    while s <= e:
        mid = (s + e) // 2
        if mid in d:
            vm_minus, vm, vm_plus = val_(mid - 1), val_(mid), val_(mid + 1)
            op_fn(min([vm_minus, vm, vm_plus]))
            flag = True
            break
        else:
            valm = val_(k, mid, n)
            d[mid] = valm
            if valm == 0:
                op_fn(0)
                flag = True
                break
            elif valm > 0:
                e = mid - 1
            else:
                s = mid + 1
    if not flag:
        val_s, val_e = abs(val_(k, s, n)), abs(val_(k, e, n))
        res = min(val_s, val_e)
        op_fn(res)
