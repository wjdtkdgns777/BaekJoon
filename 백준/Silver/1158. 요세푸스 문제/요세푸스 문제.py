from collections import deque

# N과 K 입력 받기
N, K = map(int, input().split())

# 1부터 N까지 번호가 부여된 사람들을 큐에 순서대로 저장
queue = deque(range(1, N+1))

# 요세푸스 순열을 저장할 리스트
josephus_permutation = []

# 큐에 사람이 없을 때까지 반복
while queue:
    # K-1번 사람을 큐의 뒤로 옮기고, K번째 사람을 제거
    for _ in range(K-1):
        queue.append(queue.popleft())
    # K번째 사람을 제거하고 요세푸스 순열에 추가
    josephus_permutation.append(queue.popleft())

# 요세푸스 순열 출력
print("<" + ", ".join(map(str, josephus_permutation)) + ">")
