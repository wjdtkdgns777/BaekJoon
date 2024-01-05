N, M = map(int, input().split())

# 바구니 초기화 (1부터 N까지 순서대로 번호가 매겨진 상태)
baskets = list(range(1, N + 1))

# M번의 순서 역순 만들기 과정 수행
for _ in range(M):
    i, j = map(int, input().split())
    # i번째 바구니부터 j번째 바구니까지의 순서를 역순으로 만듦
    baskets[i-1:j] = reversed(baskets[i-1:j])
    
    
for i in range(N):
    print(baskets[i],end=' ')