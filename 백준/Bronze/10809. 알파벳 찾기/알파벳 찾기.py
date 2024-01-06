# 알파벳 소문자로만 이루어진 단어 S 입력 받기
S = input()

# 알파벳 'a'부터 'z'까지 순회하면서 각 알파벳의 위치 찾기
for char in 'abcdefghijklmnopqrstuvwxyz':
    index = S.find(char)
    
    # 해당 알파벳의 위치 출력 (찾지 못한 경우 -1 출력)
    print(index, end=' ')
