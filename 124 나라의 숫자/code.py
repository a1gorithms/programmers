def solution(n):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n - 1, 3)
        rev_base += str(mod)

    
    
    rev_base = list(rev_base[::-1])
    
    for i in range(len(rev_base)):
        if rev_base[i] == '0':
            rev_base[i] = '1'
        elif rev_base[i] == '1':
            rev_base[i] = '2'
        elif rev_base[i] == '2':
            rev_base[i] = '4'
        
    
    return "".join(rev_base)