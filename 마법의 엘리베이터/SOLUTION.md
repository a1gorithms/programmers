# 마법의 엘리베이터
## 설명

## 코드
```python
def solution(storey):
    if storey < 10 :
        return min(storey, 11 - storey)
    left = storey % 10
    
    return min(left + solution(storey // 10), 10 - left + solution(storey // 10 + 1))
```