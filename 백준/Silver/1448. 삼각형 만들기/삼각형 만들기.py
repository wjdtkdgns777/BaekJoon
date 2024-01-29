import sys

N = int(sys.stdin.readline().rstrip())
straw = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
straw.sort(reverse=True)

def is_triangle (A,B,C):
  if(A+B>C and A+C>B and B+C>A):
    return True
  else:
    return False

for i in range(N):
  if i == N-2:
    print(-1)
    break
  elif(is_triangle(straw[i],straw[i+1],straw[i+2])):
    print(straw[i]+straw[i+1]+straw[i+2])
    break