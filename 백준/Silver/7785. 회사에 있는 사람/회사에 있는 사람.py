n = int(input())
log = {}

for _ in range(n):
  name,status = input().split()
  if status == "enter":
    log[name] = "enter"
  else:
    del log[name]

for name in sorted(log.keys(),reverse=True):
  print(name)