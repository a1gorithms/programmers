def solution(dots):
    
    x = dots[0][0]
    y = dots[0][1]
    
    disX = 0
    disY = 0
    
    for dot in dots[1:]:

        if x != dot[0]:
            disX = dot[0] - x
            
        if x == dot[0]:
            disY = dot[1] - y

    print(disX * disY)

solution([[1, 1], [3, 1], [1, 4], [3, 4]])