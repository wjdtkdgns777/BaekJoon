num = [list(map(int, input().split())) for _ in range(9)]

max_value = max(map(max, num))
found = False
for i in range(9):
    for j in range(9):
        if num[i][j] == max_value:
            found = True
            break
    if found:
        break

print(max_value)
print(i + 1, j + 1)
