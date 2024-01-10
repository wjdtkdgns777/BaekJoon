Char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
N, B = input().split()
B = int(B)
total_sum = 0

for i in range(len(N)):
    if N[i] in Char:
        num = 10 + Char.index(N[i])
    else:
        num = int(N[i])
    total_sum += num * (B ** (len(N) - i - 1))

print(total_sum)
