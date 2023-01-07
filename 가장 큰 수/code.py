def solution(numbers):
    
    for n in numbers:
        print(str(n) * 3)
    numbers.sort(key=lambda a : str(a) * 3, reverse=True)
    
    return str(int(''.join(map(str, numbers))))