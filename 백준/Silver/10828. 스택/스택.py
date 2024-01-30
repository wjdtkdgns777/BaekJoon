import sys

N = int(sys.stdin.readline().rstrip())
stack = []
for _ in range(N):
    user_input = sys.stdin.readline().split()
    if user_input[0] == 'push':
        stack.append(int(user_input[1]))  # 문자열을 정수로 변환
    elif user_input[0] == 'pop':
        print(stack.pop() if stack else -1)
    elif user_input[0] == 'size':
        print(len(stack))
    elif user_input[0] == 'empty':
        print(0 if stack else 1)
    elif user_input[0] == 'top':
        print(stack[-1] if stack else -1)
