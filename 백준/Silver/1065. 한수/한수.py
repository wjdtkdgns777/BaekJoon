N = int(input())

def is_hansu(num):
  if num < 100:
    return True
  else:
    num_str = str(num)
    if int(num_str[1]) - int(num_str[0]) == int(num_str[2]) - int(num_str[1]):
      return True
    else:
      return False

hansu_count = sum(is_hansu(i) for i in range(1, N+1))
print(hansu_count)