expression = input().split('-')
result = 0

first = map(int, expression[0].split('+'))
result += sum(first)


for exp in expression[1:]:
    part = map(int, exp.split('+'))
    result -= sum(part)

print(result)
