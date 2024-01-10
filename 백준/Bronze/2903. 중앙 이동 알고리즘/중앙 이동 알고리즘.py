N =int(input())
S=[0]*16


S[0]=2
S[1]=3
S[2]=5
for n in range (3,N+1):
  S[n]=2*S[n-1]-1

print(S[N]*S[N])