T = int(input())

for _ in range(T):
    N = int(input())
    note_one = set(map(int, input().split()))
    M = int(input())
    note_two = list(map(int, input().split()))

    for i in note_two:
        if i in note_one:
            print(1)
        else:
            print(0)
