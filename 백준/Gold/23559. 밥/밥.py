# 1단계: 입력 받기
n, x = map(int, input().split())  # 총 일수와 예산 입력 받기
menus = [list(map(int, input().split())) for _ in range(n)]  # 각 날짜별 메뉴의 맛 점수 입력 받기

# 2단계: 메뉴 리스트 정렬
menus_sorted = sorted(menus, key=lambda menu: menu[0] - menu[1], reverse=True)

# 3단계: 기본 예산 조정
x -= 1000 * n  # 모든 날 1,000원짜리 메뉴로 시작할 때의 예산 조정

# 4단계: 기본 맛의 합 계산
total_flavor = sum(menu[1] for menu in menus_sorted)  # 1,000원짜리 메뉴들의 맛 점수 합

# 5단계: 업그레이드 고려
for menu in menus_sorted:
    if x >= 4000 and menu[0] > menu[1]:
        total_flavor += menu[0] - menu[1]  # 5,000원짜리 메뉴로 업그레이드
        x -= 4000  # 업그레이드 비용 차감
    else:
        break  # 추가 예산이 부족하거나, 업그레이드할 가치가 없는 경우 반복 중단

# 6단계: 최종 결과 출력
print(total_flavor)
