sentence = input()

# "UCPC"를 찾기 위한 상태 변수
find = ['U', 'C', 'P', 'C']
idx = 0

for char in sentence:
    if char == find[idx]:
        idx += 1
        if idx == 4:  # "UCPC"의 모든 문자를 찾은 경우
            break

print("I love UCPC" if idx == 4 else "I hate UCPC")
