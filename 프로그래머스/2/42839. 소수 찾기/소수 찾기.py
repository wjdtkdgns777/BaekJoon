from itertools import permutations
import math

def solution(numbers):
    
    answer = 0
    def is_sosu(num):
        if num < 2:
            return False
        for i in range(2,int(math.sqrt(num))+1):
            if num%i == 0:
                return False
        return True

    perms = set()
    
    for i in range(1, len(numbers)+1):
        for p in permutations(numbers,i):
            num = int(''.join(p))
            perms.add(num)
    
    
    answer = sum(is_sosu(num) for num in perms)
    return answer