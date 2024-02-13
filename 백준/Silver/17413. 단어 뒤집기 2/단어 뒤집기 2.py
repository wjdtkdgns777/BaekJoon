s = input()
stack = []
result = ""
tag = False

for char in s:
    if char == "<":  # 태그 시작
        while stack:  # 태그 시작 전에 스택에 쌓인 문자들(단어)을 뒤집어 result에 추가
            result += stack.pop()
        tag = True
        result += char
    elif char == ">":  # 태그 끝
        tag = False
        result += char
    elif tag:  # 태그 내부인 경우
        result += char
    else:
        if char == " ":  # 공백을 만난 경우
            while stack:  # 스택에 쌓인 문자들(단어)을 뒤집어 result에 추가
                result += stack.pop()
            result += char  # 공백 추가
        else:
            stack.append(char)  # 태그 밖의 공백이 아닌 문자는 스택에 쌓음

# 입력 문자열 순회가 끝난 후 스택에 남아 있는 문자들 뒤집어 result에 추가
while stack:
    result += stack.pop()

print(result)
