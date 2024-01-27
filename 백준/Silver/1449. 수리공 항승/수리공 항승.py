N,L = map(int,input().split())
leak = list(map(int,input().split()))
leak.sort()

cover = leak[0]+L-1
tape=1

for hole in leak:
  if(hole>cover):
    cover = hole+L-1
    tape+=1

print(tape)