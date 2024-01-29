import math

N = int(input())

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

while True:
    N_str = str(N)
    if N_str == N_str[::-1] and is_prime(N):
        print(N)
        break
    N += 1
