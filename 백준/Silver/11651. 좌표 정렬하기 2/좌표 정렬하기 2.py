N = int(input())
coordinate = []
for _ in range(N):
  coordinate.append(list(map(int,input().split())))
coordinate.sort(key=lambda x:(x[1],x[0]))
for coor in coordinate:
  print(*coor)