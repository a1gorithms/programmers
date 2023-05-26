def solution(my_string, num1, num2):
    
    chr1 = my_string[num1]
    chr2 = my_string[num2]
    
    answer = list(my_string)
    
    answer[num1] = chr2
    answer[num2] = chr1
    
    
    return ''.join(answer)

solution('hello', 1, 2)