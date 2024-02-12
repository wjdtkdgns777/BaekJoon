def solution(money):
    answer = 0
    n = len(money)
    
    dp1 = [0]*(n+1)
    #마지막집 안털기
    dp2 = [0]*(n+1)
    #마지막집 털기
    
    dp1[0]=money[0]
    dp1[1]=max(money[0],money[1])
    for i in range(2,n-1):
        dp1[i]=max(dp1[i-2]+money[i],dp1[i-1])
    dp2[0] = 0
    dp2[1] = money[1]
    for i in range(2,n):
        dp2[i]=max(dp2[i-2]+money[i],dp2[i-1])
    
    answer = max(dp1[n-2],dp2[n-1])
    
    
    return answer