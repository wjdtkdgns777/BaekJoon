N = int(input())
scores = []
for _ in range(N):
    scores.append(int(input()))

count = 0
for i in range(N - 1, 0, -1):
    if scores[i-1] >= scores[i]:
        decrease = scores[i-1] - scores[i] + 1
        scores[i-1] -= decrease
        count += decrease

print(count)
