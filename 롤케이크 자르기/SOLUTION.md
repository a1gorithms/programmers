# 롤케이크 자르기

## 설명
처음에는 슬라이스로 잘라서 len(set) 으로 계속 비교를 하는 방법을 선택했다.

## 제출 코드
```python
def solution(topping):
    answer = 0
    left = {}
    right = {}
    
    for t in topping:
        if t in right:
            right[t] += 1
        else:
            right[t] = 1
    
    
    ll = 0
    rl = len(right.values())
    
    for t in topping:
        right[t] -= 1
        if right[t] == 0:
            rl -= 1
        if t in left:
            left[t] += 1
        else:
            left[t] = 1
            ll += 1
        
        if ll == rl:
            answer += 1
    
    return answer
```