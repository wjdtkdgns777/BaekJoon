def find_residents(k, n):
    residents = [i for i in range(1, n+1)]
    for floor in range(1, k+1):
        for i in range(1, n):
            residents[i] += residents[i-1]
    
    return residents[-1]


T = int(input())

for _ in range(T):
    k = int(input()) 
    n = int(input()) 
    print(find_residents(k, n))
