lines = [input() for _ in range(5)]

for i in range(15):
    for line in lines:
        if i < len(line):
            print(line[i], end='')