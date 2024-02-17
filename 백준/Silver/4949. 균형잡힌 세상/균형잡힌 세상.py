def is_valid(N):
    stack = []
    for i in N:
        if i in '([':
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1] != '(':  # 스택이 비었거나 마지막 요소가 '('가 아니면
                return False
            else:
                stack.pop()
        elif i == ']':
            if not stack or stack[-1] != '[':  # 스택이 비었거나 마지막 요소가 '['가 아니면
                return False
            else:
                stack.pop()
    
    if stack:  # 스택에 남아 있는 요소가 있으면 균형이 맞지 않음
        return False
    else:
        return True

while True:
    N = input()
    if N == '.':
        break
    print("yes" if is_valid(N) else "no")
