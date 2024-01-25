N = int(input())
members = []

for _ in range(N):
    age, name = input().split()
    age = int(age)
    members.append((age, name))

# 나이를 기준으로 정렬하되, 나이가 같으면 원래 순서를 유지
members.sort(key=lambda x: x[0])

for member in members:
    print(member[0], member[1])
