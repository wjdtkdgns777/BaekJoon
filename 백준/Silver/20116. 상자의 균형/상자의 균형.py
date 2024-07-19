n, l = map(int, input().split())
inp = list(map(int, input().split()))

result = True
s = 0
for i in range(n-1,0,-1):
    s += inp[i]
    if inp[i-1]-l < s/(n-i) < inp[i-1]+l:
        result = True
    else:
        result = False
        break
            
if result == True:
    print('stable')
else:
    print('unstable')