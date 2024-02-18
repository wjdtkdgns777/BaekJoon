from itertools import combinations

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
house = []
chicken = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken.append((i, j))
        elif city[i][j] == 1:
            house.append((i, j))

# 최소 치킨 거리 초기화
min_distance = float('inf')

# 치킨집 조합별로 도시의 치킨 거리 계산
for comb in combinations(chicken, M):
    # 현재 조합에 대한 치킨 거리 초기화
    temp = 0
    for h in house:
        # 각 집에서 현재 조합의 치킨집까지의 최소 거리 계산
        temp += min([abs(h[0] - c[0]) + abs(h[1] - c[1]) for c in comb])
    # 도시의 치킨 거리 최소값 업데이트
    min_distance = min(min_distance, temp)

print(min_distance)
