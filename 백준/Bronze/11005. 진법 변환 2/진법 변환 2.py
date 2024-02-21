def convert_to_base(n, b):
  # 변환된 숫자를 저장할 문자열
  result = ''
  
  # n이 0보다 클 때까지 반복하여 10진수 n을 b진수로 변환
  while n > 0:
      # n을 b로 나눈 나머지를 구함
      remainder = n % b

      if remainder < 10:
          # 나머지가 10보다 작으면 숫자 그대로 사용
          result = str(remainder) + result
      else:
          # 나머지가 10 이상이면, 알파벳 대문자를 사용
          # A: 10, B: 11, ..., Z: 35에 해당하므로, 
          # 아스키 코드를 사용하여 숫자에 55를 더한 값을 문자로 변환
          result = chr(remainder + 55) + result

      # n을 b로 나눈 몫으로 업데이트하여 다음 자리수 계산을 준비
      n //= b

  return result

N, B = map(int,input().split())
print(convert_to_base(N, B))