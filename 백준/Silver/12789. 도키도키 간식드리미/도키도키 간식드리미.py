N = int(input())
students = list(map(int, input().split()))
stack = []
current = 1

for student in students:
    if student == current:
        current += 1
    else:
        while stack and stack[-1] == current:
            stack.pop()
            current += 1
        if stack and stack[-1] < student:
            print("Sad")
            break
        stack.append(student)
else:
    while stack:
        if stack.pop() != current:
            print("Sad")
            break
        current += 1
    else:
        print("Nice")
