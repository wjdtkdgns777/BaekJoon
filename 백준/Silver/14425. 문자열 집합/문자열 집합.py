N, M = map(int, input().split())
word = set()  
word_test = [] 
count = 0

for _ in range(N):
    word.add(input())

for _ in range(M):
    word_test.append(input())

for test_str in word_test:
    if test_str in word:
        count += 1

print(count)
