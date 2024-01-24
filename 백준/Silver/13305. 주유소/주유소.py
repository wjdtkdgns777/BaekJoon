N = int(input())
road = list(map(int, input().split()))
oil_price = list(map(int, input().split()))

total_cost = 0  # 총 비용
min_price = oil_price[0]  # 현재까지 가장 저렴한 기름 가격

for i in range(N-1):
    # 가장 저렴한 기름 가격으로 주유
    if oil_price[i] < min_price:
        min_price = oil_price[i]
    total_cost += min_price * road[i]

print(total_cost)
