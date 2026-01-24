in_fn = input
op_fn = print


def read_str() -> str:
    return in_fn().strip()

s = read_str()
stack = []
for c in s:
    if not stack:
        stack.append(c)
    else:
        if stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
op_fn("".join(stack))

