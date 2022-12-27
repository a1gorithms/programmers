def solution(n):
    f = 1
    s = 2
    t = 0
    
    if n == 1:
        return f
    if n == 2:
        return s
    
    for i in range(3, n + 1):
        t = (f + s) % 1000000007
        f = s
        s = t
    return t