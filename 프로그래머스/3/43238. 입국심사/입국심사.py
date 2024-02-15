def solution(n, times):
    minTime = 1
    maxTime = max(times) * n  # 모든 사람이 가장 오래 걸리는 심사대에서 심사받는 경우

    while minTime <= maxTime:
        mid = (minTime + maxTime) // 2  # 중간값 계산
        total = sum(mid // time for time in times)  # 중간값 시간 동안 심사할 수 있는 총 인원 수

        if total >= n:  # 모든 사람을 심사할 수 있는 경우
            answer = mid
            maxTime = mid - 1
        else:  # 그렇지 않은 경우
            minTime = mid + 1

    return answer
