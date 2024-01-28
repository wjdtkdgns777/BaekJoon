N = int(input())
tree = list(map(int, input().split()))
tree.sort(reverse=True)
max_day = 0

for i in range(N):
    if max_day < tree[i] + i + 2:
        max_day = tree[i] + i + 2

print(max_day)
