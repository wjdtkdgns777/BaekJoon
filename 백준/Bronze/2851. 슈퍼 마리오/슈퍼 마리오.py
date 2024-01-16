closest = 0
total = 0

for _ in range(10):
    mushroom = int(input())
    total += mushroom

    if abs(100 - total) <= abs(100 - closest):
        closest = total

print(closest)
