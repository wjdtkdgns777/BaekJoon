n, m = map(int, input().split())
dnas = [input() for _ in range(n)]  # DNA 문자열 입력받기

result = ''  # 최종 DNA 문자열
sum_hamming = 0  # Hamming Distance 합계

# 각 위치별로 뉴클레오티드의 빈도수를 계산합니다.
for i in range(m):
    a, c, g, t = 0, 0, 0, 0  # 뉴클레오티드별 출현 횟수

    # 각 DNA에서 해당 위치의 뉴클레오티드 빈도수를 계산
    for dna in dnas:
        if dna[i] == 'A':
            a += 1
        elif dna[i] == 'C':
            c += 1
        elif dna[i] == 'G':
            g += 1
        elif dna[i] == 'T':
            t += 1

    # 가장 많이 출현하는 뉴클레오티드를 선택하고, Hamming Distance를 합계에 더합니다.
    max_count = max(a, c, g, t)
    if max_count == a:
        result += 'A'
        sum_hamming += (c + g + t)
    elif max_count == c:
        result += 'C'
        sum_hamming += (a + g + t)
    elif max_count == g:
        result += 'G'
        sum_hamming += (a + c + t)
    elif max_count == t:
        result += 'T'
        sum_hamming += (a + c + g)

# 결과 출력
print(result)
print(sum_hamming)
