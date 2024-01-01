n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

# 맨 위층부터 시작하여 아래층으로 내려가며 최대 합 계산
for i in range(1, n):
    for j in range(len(triangle[i])):
        # 대각선 왼쪽과 오른쪽의 최대값을 더해 현재 위치를 갱신
        if j == 0:
            triangle[i][j] += triangle[i - 1][j]
        elif j == len(triangle[i]) - 1:
            triangle[i][j] += triangle[i - 1][j - 1]
        else:
            triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])

# 마지막 행의 최대값이 최대 합
print(max(triangle[-1]))
