from itertools import permutations

# 숫자 입력 받기
N = int(input())
nums = list(map(int, input().split()))

# 연산자 입력 받기
add, sub, mul, div = map(int, input().split())
operators = ['+'] * add + ['-'] * sub + ['*'] * mul + ['/'] * div

# 가능한 모든 연산자 조합 생성
op_combinations = set(permutations(operators, N - 1))

# 계산 실행 및 결과 찾기
max_result = float("-inf")
min_result = float("inf")

for ops in op_combinations:
    result = nums[0]
    for i in range(1, N):
        if ops[i - 1] == '+':
            result += nums[i]
        elif ops[i - 1] == '-':
            result -= nums[i]
        elif ops[i - 1] == '*':
            result *= nums[i]
        else:  # 나눗셈
            if result < 0:
                result = -(-result // nums[i])  # 음수 나눗셈 처리
            else:
                result //= nums[i]
    max_result = max(max_result, result)
    min_result = min(min_result, result)

# 결과 출력
print(max_result)
print(min_result)