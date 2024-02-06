from itertools import combinations

while True:
    # 한 줄을 읽어서 공백으로 분할
    input_line = input().split()
    # 분할된 리스트의 첫 번째 원소를 정수로 변환하여 K에 할당
    K = int(input_line[0])
    if K == 0:
        break
    # 리스트의 첫 번째 원소를 제외한 나머지를 정수로 변환하여 S에 할당
    S = list(map(int, input_line[1:]))
    # combinations 함수를 사용하여 S에서 6개를 고르는 모든 조합 계산
    com = list(combinations(S, 6))
    
    # 계산된 조합을 출력
    for combo in com:
        print(' '.join(map(str, combo)))
    
    # 각 테스트 케이스 사이에 빈 줄 출력
    print()
