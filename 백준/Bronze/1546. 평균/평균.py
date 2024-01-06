N = int(input())
score = list(map(int,input().split()))
max = max(score)
avg = sum(score)/N

print(avg/max*100)