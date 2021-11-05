def solution(absolutes, signs):
    answer = 0
    
    for i, number in enumerate(absolutes):
        if signs[i] is False:
            number *= -1
        answer += number
        
    return answer