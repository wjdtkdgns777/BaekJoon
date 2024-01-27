board = input().strip()
i = 0
result = []

while i < len(board):  # 보드의 전체 길이를 순회합니다.
    if board[i] == 'X':  # 'X'를 만났을 때
        count = 0
        # 연속된 'X'의 길이를 세는 부분입니다.
        while i < len(board) and board[i] == 'X':
            i += 1
            count += 1
        
        if count % 2 != 0:  # 연속된 'X'의 길이가 홀수라면 덮을 수 없습니다.
            result = -1
            break

        # 연속된 'X'의 길이가 짝수라면, 'AAAA'와 'BB'로 덮습니다.
        result.append('AAAA' * (count // 4) + 'BB' * ((count % 4) // 2))
    else:  # 'X'가 아닌 다른 문자('.')
        result.append('.')
        i += 1

# 결과 출력: 모든 'X'를 덮었거나, 덮을 수 없는 경우 -1을 출력합니다.
print(''.join(map(str, result)) if result != -1 else -1)
