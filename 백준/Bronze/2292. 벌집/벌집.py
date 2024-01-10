N = int(input())
level = 1  # 중앙의 1번 방부터 시작
max_number_in_level = 1  # 현재 레벨에서의 최대 방 번호

while N > max_number_in_level:
    max_number_in_level += 6 * level  # 다음 레벨로 이동할 때마다 6의 배수만큼 증가
    level += 1  # 레벨 증가

print(level)
