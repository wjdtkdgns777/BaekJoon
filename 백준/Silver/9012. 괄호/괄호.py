T = int(input())

for _ in range(T):
    ps = input()
    stack = []
    is_vps = True

    for ch in ps:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if not stack:
                is_vps = False
                break
            stack.pop()

    if stack:
        is_vps = False

    print("YES" if is_vps else "NO")
