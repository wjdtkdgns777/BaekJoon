def minimize_S(N, A, B):
    # A를 오름차순으로 정렬
    A.sort()

    # B의 원소에 대응하는 A의 요소들의 인덱스를 얻기 위해 B를 인덱스와 함께 정렬
    idx_B = sorted(range(N), key=lambda x: B[x], reverse=True)

    # S 계산
    S = 0
    for i in range(N):
        S += A[i] * B[idx_B[i]]
    return S

# 입력 처리
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 결과 출력
print(minimize_S(N, A, B))
