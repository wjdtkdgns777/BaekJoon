T = int(input())
count = 0
for _ in range(T):
    ab = input()
    stack = []
    for char in ab:
        if stack and stack[-1] == char:  # 스택의 마지막 문자와 현재 문자가 같으면 짝을 이룰 수 있음
            stack.pop()
        else:
            stack.append(char)
    if not stack:  # 스택이 비어있으면 모든 문자가 짝을 이룸
        count += 1

print(count)
