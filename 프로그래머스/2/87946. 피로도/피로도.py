from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for dungeon_order in permutations(dungeons, len(dungeons)):
        current_k = k
        count = 0
        for min_fatigue,use_fatigue in dungeon_order:
            if current_k>=min_fatigue:
                current_k=current_k-use_fatigue
                count+=1
            else:
                break
        answer = max(answer, count)
                
        
    
    return answer