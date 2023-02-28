# 택배상자

## 코드
```python
from collections import deque

def solution(order):
    answer = 0
    boxs = range(1, len(order) + 1)
    sub = []
    order = deque(order)
    for box in boxs:
        if sub and order[0] == sub[-1]:
            sub.pop()
            answer += 1
            order.popleft()
        if box == order[0]:
            order.popleft()
            answer += 1
        else:
            sub.append(box)

    while sub:
        if sub.pop() == order[0]:
            order.popleft()
            answer += 1
        else:
            break
        
    return answer
```
깔끔한 코드
```python
def solution(order):
    answer = 0
    stacks = []
    N = len(order)
    i = 1
    idx = 0
    while i < N+1:
        stacks.append(i)
        while stacks[-1] == order[idx]:
            idx += 1
            stacks.pop()
            if len(stacks) == 0:
                break
        i += 1


    return idx
```