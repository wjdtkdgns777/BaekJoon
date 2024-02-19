def solution(n, s):
    if n > s:
        return [-1]  # 조건을 만족하는 집합이 존재하지 않는 경우
    
    # 기본값 설정
    base_value = s // n  # 평균값
    remainder = s % n  # 나머지
    
    # 기본 집합 구성
    answer = [base_value] * n
    
    # 나머지를 집합의 원소들에 분배
    for i in range(remainder):
        answer[i] += 1
    
    # 오름차순 정렬을 위한 정렬
    answer.sort()
    
    return answer
