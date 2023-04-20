def solution(hp):
    
    count = 0
    
    if hp >= 5:
        count += hp // 5
        hp = hp % 5
        
    if hp >= 3:
        count += hp // 3
        hp = hp % 3
        
    if hp >= 1:
        count += hp // 1
        hp = hp % 1
        
    return count

https://school.programmers.co.kr/learn/courses/30/lessons/120837

