S = input()
mini_s = set()

for i in range(len(S)):
    for j in range(i, len(S)):
        mini_s.add(S[i:j+1])

print(len(mini_s))
