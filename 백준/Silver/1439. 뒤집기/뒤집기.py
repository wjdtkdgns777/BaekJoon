from collections import deque

N = input()
q = deque()

# 첫 번째 문자를 deque에 추가
q.append(N[0])

# 문자열의 두 번째 문자부터 마지막 문자까지 확인
for i in range(1, len(N)):
    # 이전 문자와 다를 때만 deque에 추가
    if N[i] != N[i-1]:
        q.append(N[i])

# 0과 1의 개수 세기
sum_zero = q.count('0')
sum_one = q.count('1')

# 더 적은 개수 출력
print(min(sum_zero, sum_one))
