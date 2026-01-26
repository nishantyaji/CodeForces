in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


base = 1000000007


# Strings of the form D***** are of 3^(n-1) in number
# But to close the loop on the last move to D we have to discount
# in 3^(n-1) the answers that end with D in penultimate position i.e. dp[n-1]
# Therefore dp[n] = 3^(n-1)-dp[n-1]
# recursively dp[n] = 3^(n-1) - 3^(n-2) + ...

def sum_odd_pow_3(limit_pow: int):
    pow9 = (limit_pow - 1) // 2
    val = 3 * (pow(9, pow9 + 1, base) - 1) * pow(8, -1, base)
    return val % base


def sum_even_pow_3(limit_pow: int):
    pow9 = (limit_pow - 2) // 2
    val = 9 * (pow(9, pow9 + 1, base) - 1) * pow(8, -1, base)
    return val % base


n = read_int()

if n % 2 == 0:
    res = (sum_odd_pow_3(n - 1) - sum_even_pow_3(n - 2)) % base
else:
    res = (sum_even_pow_3(n - 1) - sum_odd_pow_3(n - 2)) % base
op_fn(res)
