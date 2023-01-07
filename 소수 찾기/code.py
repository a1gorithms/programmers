import itertools

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
        
def solution(numbers):
    answer = 0
    buf = []
    nbs = list(numbers)
    for l in range(len(nbs)):
        for i in itertools.permutations(nbs, l + 1):
            # print(i)
            p = int("".join(i))
            if isPrime(p) and p not in buf:
                answer += 1
                buf.append(p)
    return answer