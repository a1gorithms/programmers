# 내가 푼 풀이
def solution(n):
    array = []
    
    for i in range(1, n+1) :
        if i%2 != 0 :
            array.append(i)
            
    return array

# 인상 깊은 풀이
def solution(n):
    return [i for i in range(1, n+1, 2)]
            