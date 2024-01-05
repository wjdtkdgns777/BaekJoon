# 제출한 학생들의 출석번호를 저장할 집합
submitted = set()

# 제출한 학생들의 출석번호 입력받음
for _ in range(28):
    number = int(input())
    submitted.add(number)

# 제출하지 않은 학생들의 출석번호를 찾아서 정렬
not_submitted = sorted(set(range(1, 31)) - submitted)

# 결과 출력
for number in not_submitted:
    print(number)
