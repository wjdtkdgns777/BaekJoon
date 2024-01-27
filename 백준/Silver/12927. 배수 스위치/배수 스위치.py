N = input()
bulbs = list(N)
count = 0

for i in range(len(bulbs)):
    if bulbs[i] == 'Y':
        count += 1
        for j in range(i, len(bulbs), i+1):
            bulbs[j] = 'N' if bulbs[j] == 'Y' else 'Y'

# 모든 전구가 꺼져있는지 확인
if all(bulb == 'N' for bulb in bulbs):
    print(count)
else:
    print(-1)
