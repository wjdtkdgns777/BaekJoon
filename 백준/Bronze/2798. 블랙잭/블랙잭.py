from itertools import combinations

def blackjack(N,M,cards):
  max_sum = 0
  for combo in combinations(cards,3):
    temp_sum = sum(combo)
    if max_sum<temp_sum<=M:
      max_sum=temp_sum
  return max_sum

N,M = map(int,input().split())
cards = list(map(int,input().split()))

print(blackjack(N,M,cards))