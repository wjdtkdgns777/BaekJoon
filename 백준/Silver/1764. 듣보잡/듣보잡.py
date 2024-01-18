N, M = map(int, input().split())
never_heard = {input() for _ in range(N)}
never_seen = {input() for _ in range(M)}

# 듣도 보도 못한 사람들의 명단 찾기
never_people = sorted(list(never_heard & never_seen))

# 듣보잡의 수 출력
print(len(never_people))

# 듣보잡의 명단 출력
for name in never_people:
    print(name)
