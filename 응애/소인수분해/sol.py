def solution(n):
    count = 2
    answer = []
    
    while n > 1:
        if n % count == 0:
            n = n / count
            answer.append(count)
        else: count += 1
        
    return sorted(list(set(answer)))
