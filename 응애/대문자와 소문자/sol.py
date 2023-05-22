def solution(my_string):
    
    answer = ''
    
    for i in my_string:
        if ord(i) > 90:
            answer = answer + chr(ord(i) - 32)
        elif ord(i) < 91: 
            answer = answer + chr(ord(i) + 32)
        
    return(answer)
