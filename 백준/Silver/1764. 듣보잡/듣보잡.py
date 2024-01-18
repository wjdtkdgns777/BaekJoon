N,M = map(int,input().split())
never_heard = set(input() for _ in range(N))
never_seen = set(input() for _ in range(M))

never_people = []

for people in never_heard:
  if people in never_seen:
    never_people.append(people)

never_people.sort()

print(len(never_people))
for i in range(len(never_people)):
  print(never_people[i])