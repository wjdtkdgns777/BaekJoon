def solution(triangle):
    # 삼각형의 높이
    height = len(triangle)
    
    # 삼각형의 바닥부터 시작하여 위로 올라가면서 최대 합 계산
    for i in range(height-2, -1, -1):  # 바닥에서 두 번째 층부터 시작하여 꼭대기까지
        for j in range(i+1):  # 각 층에 있는 요소들에 대해
            # 현재 위치에서 내려갈 수 있는 두 경로 중 더 큰 합을 선택
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
    
    # 삼각형 꼭대기의 값이 최대 합
    return triangle[0][0]
