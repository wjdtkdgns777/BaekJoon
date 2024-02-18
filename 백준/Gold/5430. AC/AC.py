from collections import deque

T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    array_input = input()[1:-1]  # 대괄호를 제외하고 슬라이싱
    if n > 0:
        numbers = deque(map(int, array_input.split(',')))
    else:
        numbers = deque()  # 빈 deque 생성

    is_valid = True
    is_reversed = False  # 배열의 뒤집힌 상태를 추적

    for cmd in p:
        if cmd == 'R':
            is_reversed = not is_reversed  # 뒤집힌 상태 토글
        elif cmd == 'D':
            if numbers:
                if is_reversed:
                    numbers.pop()  # 뒤집힌 상태에서는 마지막 요소를 제거
                else:
                    numbers.popleft()  # 정상 상태에서는 첫 번째 요소를 제거
            else:
                is_valid = False
                break

    if is_reversed:
        numbers.reverse()  # 최종적으로 뒤집힌 상태라면 뒤집기

    if is_valid:
        print('[' + ','.join(map(str, numbers)) + ']')
    else:
        print('error')
