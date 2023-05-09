def solution(my_string):
    
    numbers = ''.join(list(filter(str.isdigit, my_string)))
    
    answer = [int(a) for a in str(numbers)]
    answer.sort()
    
    return answer