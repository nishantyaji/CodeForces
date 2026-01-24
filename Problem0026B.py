in_fn = input
op_fn = print


def read_str() -> str:
    return in_fn().strip()


stack = []
s = read_str()
for c in s:
    if not stack:
        stack.append(c)
    else:
        if c == ")" and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(c)
op_fn((len(s) - len(stack)))
