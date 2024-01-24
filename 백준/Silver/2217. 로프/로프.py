N = int(input())
ropes = [] 

for _ in range(N):
    ropes.append(int(input()))  

ropes.sort(reverse=True)

max_weight = 0
for i in range(N):
    weight = ropes[i] * (i + 1)
    if weight > max_weight:
        max_weight = weight

print(max_weight)
