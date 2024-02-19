import heapq

def solution(n, works):
    # 작업량이 많은 순으로 처리하기 위해 최대 힙을 사용
    # works의 각 원소에 -1을 곱해 최소 힙을 최대 힙처럼 사용
    works = [-work for work in works]
    heapq.heapify(works)
    
    while n > 0 and works:
        # 가장 큰 작업량을 하나 줄임
        work = heapq.heappop(works) + 1
        if work < 0:
            heapq.heappush(works, work)
        n -= 1
    
    # 야근 피로도 계산: 남은 작업량의 제곱합
    return sum(work ** 2 for work in works)
