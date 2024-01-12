
N = int(input())

def find_constructor(N):
    for i in range(1, N):
        digit_sum = 0
        number = i
        while number > 0:
            number, digit = divmod(number, 10)
            digit_sum += digit
        if i + digit_sum == N:
            return i
    return 0

print(find_constructor(N))
