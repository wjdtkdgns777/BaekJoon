N = int(input())
M = int(input())
VIP = [int(input()) for _ in range(M)] + [N+1]
dp = [1, 1] + [0]*(N-1)

# 피보나치 수열을 이용하여 dp 테이블 채우기
for i in range(2, N+1):
    dp[i] = dp[i-1] + dp[i-2]

prev = 0
answer = 1
for vip in VIP:
    answer *= dp[vip - prev - 1]
    prev = vip

print(answer)
