N = int(input())
house = list(map(int, input().split()))
house.sort()

# 중앙값을 찾아 출력합니다.
# 짝수 개일 경우 두 중앙값 중 작은 값을 선택합니다.
median_index = (N - 1) // 2
print(house[median_index])
