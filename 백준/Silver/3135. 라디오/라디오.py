A, B = map(int, input().split())
N = int(input())
dial = [int(input()) for _ in range(N)]
dial.append(A)  # 현재 주파수도 즐겨찾기에 추가하여 고려

min_button_press = abs(A - B)  # 직접 버튼을 사용하는 경우의 버튼 수

for favorite in dial:
    # 즐겨찾기 버튼을 사용하는 경우의 버튼 수 계산
    button_press = 1 + abs(favorite - B) 
    min_button_press = min(min_button_press, button_press)

print(min_button_press)
