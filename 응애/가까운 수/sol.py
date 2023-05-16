def solution(array, n):
    
    temp = 1000
    count = 0
    
    for i in range(len(array)):
        if temp > abs(array[i] - n):
            temp = abs(array[i] - n)
            count = i
            
        elif temp == abs(array[i] - n):
            if array[count] > array[i]:
                count = i
            
    return array[count]