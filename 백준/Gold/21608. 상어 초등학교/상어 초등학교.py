N = int(input())
students = [list(map(int,input().split())) for _ in range(N**2)]
data = [[0]*N for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for student in students:
  student_id = student[0]
  preferences = student[1:]
  available = []

  for i in range(N):
    for j in range(N):
      if data[i][j] == 0:
        prefer, empty = 0,0
        for k in range(4):
          nx,ny = i+dx[k], j+dy[k]
          if 0<=nx<N and 0<=ny<N:
            if data[nx][ny] in preferences:
              prefer+=1
            if data[nx][ny] ==0:
              empty += 1
        available.append((prefer,empty,i,j))
  available.sort(key = lambda x:(-x[0],-x[1],-x[2],-x[3]))
  _,_,best_i,best_j=available[0]
  data[best_i][best_j] = student_id
score = [0,1,10,100,1000]
student_dict = {student[0]: student[1:] for student in students}
answer = 0
for i in range(N):
    for j in range(N):
        student_id = data[i][j]  
        preferences = student_dict[student_id] 
        count = 0 
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            if 0 <= nx < N and 0 <= ny < N and data[nx][ny] in preferences:
                count += 1
        answer += score[count]
print(answer)