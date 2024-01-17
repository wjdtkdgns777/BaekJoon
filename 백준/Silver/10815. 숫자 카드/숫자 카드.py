N = int(input())
number = set(map(int, input().split()))  # 숫자들을 set으로 변환하여 저장
M = int(input())
check_number = list(map(int, input().split()))

for i in check_number:
    print(1 if i in number else 0, end=" ")
