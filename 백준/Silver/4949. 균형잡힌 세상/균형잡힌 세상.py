while True:
    words = input()
    if words == '.':
        break

    stack = []
    is_valid = True

    for word in words:
        if word in '([':
            stack.append(word)
        elif word == ')':
            if not stack or stack[-1] == '[':
                is_valid = False
                break
            stack.pop()
        elif word == ']':
            if not stack or stack[-1] == '(':
                is_valid = False
                break
            stack.pop()

    if is_valid and not stack:
        print("yes")
    else:
        print("no")
