def solution(quiz):
    
    answer=  []
    
    for i in quiz:
        result = 0
        a = i.split()
        
        if a[1] == '+':
            result = int(a[0]) + int(a[2])
        else : result = int(a[0]) - int(a[2])
        
        if result == int(a[4]):
            answer.append('O')
        else : answer.append('X')
        
    return answer
            
    