def solution(my_str, n):
    answer = []
    itr = 0
    start = 0
    end = n
    
    if len(my_str) % n == 0:
        itr = len(my_str) // n
    else : itr = (len(my_str) // n) + 1
    
    for i in range(itr):
        answer.append(my_str[start:end])
        start += n
        end += n
        
    return answer