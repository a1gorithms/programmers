def solution(num, k):
    
    for i, value in enumerate(str(num)):
        if value == str(k):
            return i + 1
        
    return -1
    
