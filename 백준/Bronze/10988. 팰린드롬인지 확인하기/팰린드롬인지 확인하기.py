word = input()

# 문자열을 슬라이싱으로 역순으로 만들어 비교
if word == word[::-1]:
    print(1)
else:
    print(0)