N = int(input())
meeting = []

for _ in range(N):
  start,end = map(int,input().split())
  meeting.append((start,end))

def max_meeting(meeting):
  meeting.sort(key=lambda x:(x[1],x[0]))
  last_end_time = 0
  selected_meeting = 0

  for start,end in meeting:
    if start >= last_end_time:
      selected_meeting +=1
      last_end_time = end

  return selected_meeting

print(max_meeting(meeting))