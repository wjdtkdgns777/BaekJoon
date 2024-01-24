S = int(input())
total = 0
N = 0

while total <= S:
    N += 1
    total += N

# 마지막에 더한 N이 합을 S를 초과하게 만들었으므로 N-1이 정답
print(N-1)
