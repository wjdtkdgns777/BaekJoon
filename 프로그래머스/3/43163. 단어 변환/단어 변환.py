from collections import deque

def word_diff(word1, word2):
    return sum(1 for a, b in zip(word1, word2) if a != b)

def solution(begin, target, words):
    if target not in words:
        return 0
    queue = deque([(begin, 0)])
    visited = set([begin])
    while queue:
        current_word, step = queue.popleft()
        if current_word == target:  # 오타 수정됨
            return step
        for word in words:
            if word_diff(current_word, word) == 1 and word not in visited:
                visited.add(word)
                queue.append((word, step + 1))
    return 0
