def solution(people, limit):
    answer = 0
    right = len(people)-1
    left = 0
    people.sort()
    while right >= left:
        if people[left]+people[right]>limit:
            right -= 1
            answer += 1
        else:
            right -= 1
            left += 1
            answer +=1
    
    return answer