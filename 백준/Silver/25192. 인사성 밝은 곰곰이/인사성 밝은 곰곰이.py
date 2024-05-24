N = int(input())
users = set()
count = 0
for _ in range(N):
  record = input()
  if record == "ENTER":
    users.clear()
  elif record not in users:
    users.add(record)
    count += 1

print(count)