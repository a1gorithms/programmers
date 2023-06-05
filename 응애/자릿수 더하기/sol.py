def solution(n):
    string = str(n)
    answer = 0
    
    for i in string:
        answer += int(i)
        
    return answer