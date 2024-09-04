in_fn = input
op_fn = print

num_tests = int(in_fn())
tests = []
for n_t in range(num_tests):
    [n, k, q] = list(map(int, in_fn().split()))
    arr = list(map(int, in_fn().split()))
    queries = []
    for _ in range(q):
        queries.append(list(map(int, in_fn().split())))
    tests.append([k, arr, queries])


def rem_(d: dict, numm: int):
    if numm in d:
        if d[numm] == 1:
            del d[numm]
        else:
            d[numm] = d[numm] - 1


def add_(d: dict, numm: int):
    if numm in d:
        d[numm] = d[numm] + 1
    else:
        d[numm] = 1


for [k, arr2, queries] in tests:
    arr = [x - i for i, x in enumerate(arr2)]
    mp = dict()
    for i in range(k):
        add_(mp, arr[i])
    res = [k - max([v for k, v in mp.items()])]
    for i in range(k, len(arr)):
        rem_(mp, arr[i - k])
        add_(mp, arr[i])
        res.append((k - max([v for k, v in mp.items()])))

    for [l, r] in queries:
        op_fn(res[l - 1])
