sz = int(input())

arr, prev, res = [], "", 0
for i in range(sz):
    inp = input()
    if inp != prev:
        res += 1
    prev = inp
print(res)

