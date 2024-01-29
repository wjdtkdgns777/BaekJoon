A, B = input().split()

def word_diff(C, D):
    count = 0
    for c, d in zip(C, D):
        if c != d:
            count += 1
    return count

# 최소 차이를 최대 문자열 길이로 초기화
min_diff = len(B)
len_diff = len(B) - len(A)

# B의 각 부분 문자열과 A를 비교하여 최소 차이를 찾음
for i in range(len_diff + 1):
    diff = word_diff(A, B[i:i + len(A)])
    min_diff = min(min_diff, diff)

print(min_diff)
