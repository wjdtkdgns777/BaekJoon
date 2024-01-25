N = int(input())
words = set()

for _ in range(N):
    words.add(input())

# 길이가 짧은 것부터, 길이가 같으면 사전 순으로 정렬
sorted_words = sorted(words, key=lambda x: (len(x), x))

for word in sorted_words:
    print(word)
