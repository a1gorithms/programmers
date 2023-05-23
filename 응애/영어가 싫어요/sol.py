def solution(numbers):
    dic = {
        'zero': '0','one': '1','two': '2','three': '3', 'four': '4','five': '5','six': '6',
        'seven': '7','eight': '8','nine': '9'
    } 
    buf = ''
    answer = ''
    
    for i in numbers:
        buf += i
        if buf in dic:
            answer += dic[buf]
            buf = ''
        
    return int(answer)