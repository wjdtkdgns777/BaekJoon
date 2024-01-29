N, M = map(int, input().split())
costs = [int(input()) for _ in range(M)]
costs.sort(reverse=True)

max_value = 0
best_price = 0

for i in range(M):
    # 달걀 수량을 초과하지 않도록 최소값 사용
    eggs_sold = min(i + 1, N)
    revenue = costs[i] * eggs_sold

    if revenue > max_value:
        max_value = revenue
        best_price = costs[i]

print(best_price, max_value)
