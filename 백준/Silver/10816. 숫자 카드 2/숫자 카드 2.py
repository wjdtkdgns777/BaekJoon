N = int(input())
cards = list(map(int, input().split()))
M = int(input())
numbers_to_check = list(map(int, input().split()))

card_count = {}
for card in cards:
    if card in card_count:
        card_count[card] += 1
    else:
        card_count[card] = 1

result = []
for number in numbers_to_check:
    result.append(str(card_count.get(number, 0)))

print(' '.join(result))
