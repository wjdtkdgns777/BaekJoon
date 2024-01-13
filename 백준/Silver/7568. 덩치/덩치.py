N = int(input())
people = []

for _ in range(N):
    weight, height = map(int, input().split())
    people.append((weight, height))

ranks = [1] * N  # 모든 사람의 등수를 1로 초기화

for i in range(N):
    for j in range(N):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            ranks[i] += 1

for rank in ranks:
    print(rank, end=' ')
