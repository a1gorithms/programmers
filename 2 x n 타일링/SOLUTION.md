# 2 X n 타일링

dp로 풀리는 문제이다.

dp[3] 는 dp[2] 에 | 블럭을  추가한 것과 dp[1] 에 ㅡ 블럭을 2개 쌓은 것을 추가한 것과 같다. 
(dp[1] 에 || 블럭을 추가한 것은 dp[2]에 | 추가 한 것과 중복되어 고려하지 않는다.)
```python
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
```