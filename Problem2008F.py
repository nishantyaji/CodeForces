import math

num_tests = int(input())
tests = []
for n_t in range(num_tests):
    l = input()
    ls = list(map(int, input().split()))
    tests.append(ls)

# tests = [[3, 2, 3], [2, 2, 2, 4], [1, 2, 3, 4, 5]]

for t in tests:
    n = len(t)
    total = sum(t)
    nume = total * total - sum([x * x for x in t])
    deno = (n * (n - 1))
    g = math.gcd(nume, deno)
    num, den = nume // g, deno // g
    base = 1000000007
    den_inv = pow(den, base - 2, base)
    val = (num * den_inv) % base
    print(val)
