num_tests = int(input())
tests = []
for n_t in range(num_tests):
    # l = input()
    [n, k] = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    tests.append([k, arr])

for [k, arr] in tests:
    arr.sort(reverse=True)
    diff = 0
    for i in range(0, len(arr), 2):
        secnd = 0 if i + 1 == len(arr) else arr[i + 1]
        diff += arr[i] - secnd

    # Another loop is not required when arr is of even length
    # we can do the below block in o(1) then because
    # we know that the diff come from pairs
    # because in even length arr there is no sore thumb
    for i in range(1, len(arr), 2):
        if k == 0:
            break
        this_diff = arr[i - 1] - arr[i]
        this_ans = min(this_diff, k)
        diff -= this_ans
        k -= this_ans

    print(diff)
