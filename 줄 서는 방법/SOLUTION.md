# 줄 서는 방법
## 설명
처음 코드
```python
def solution(n, k):
    cases = []
    
    def dfs(ll):
        if len(cases) == k:
            return cases[-1]
        if n == len(ll):
            cases.append(ll)
        for i in range(n):
            if (i + 1) not in ll:
                dfs(ll + [i + 1])
    dfs([])
    
    return cases[k - 1]
    
```
이렇게 풀면 시간 초과 난다. 


## 코드
```python
from math import factorial as fac

def solution(n, k):
    k -= 1
    l = list(range(1, n+1))
    answer = []
    while l:
        idx, k = divmod(k, fac(len(l)-1))
        answer.append(l.pop(idx))
    return answer
```