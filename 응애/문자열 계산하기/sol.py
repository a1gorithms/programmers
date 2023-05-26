def solution(my_string):
    
    my_list = my_string.split()
    answer = int(my_list[0])
    
    for i, value in enumerate(my_list):
        if value == '+':
            answer += int(my_list[i + 1])
        elif value == '-':
            answer -= int(my_list[i + 1])
            
    return answer
            
            