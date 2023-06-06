def solution(array, height):
    
    answer = sorted(array, reverse = True)
    count = 0
    
    for i in answer:
        if i > height:
            count += 1
    return count