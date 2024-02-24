from collections import Counter

# 책의 개수 N 입력 받기
N = int(input())

# N개의 책 제목을 입력 받아 리스트에 저장
books = [input() for _ in range(N)]

# 책 제목별 판매 횟수를 계산
book_counts = Counter(books)

# 가장 많이 판매된 책의 제목(들)과 그 판매 횟수 찾기
max_count = max(book_counts.values())
best_sellers = [book for book, count in book_counts.items() if count == max_count]

# 사전 순으로 가장 앞서는 책의 제목 출력
print(sorted(best_sellers)[0])