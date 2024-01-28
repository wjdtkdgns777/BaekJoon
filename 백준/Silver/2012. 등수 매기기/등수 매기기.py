import sys

n = int(sys.stdin.readline().strip())
expected = [int(sys.stdin.readline().strip()) for _ in range(n)]
expected.sort()

result = 0
for i in range(1, n + 1):
    result += abs(i - expected[i - 1])
print(result)
