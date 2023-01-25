# 두 큐 합 같게 만들기
## 설명
두 큐의 합을 같게 만들려면 한 개의 큐에 들어 있는 값의 합이 전체 큐 값의 합의 1/2 과 같아야한다.

그래서 두 큐를 붙인 다음 `s` 와 `e` 정의하고 s와 e 만큼 자른 리스트의 합이 전체 큐 값의 합의 1/2이 되는 s, e 변화 횟수를 찾으면 된다.

처음에 `sum()` 함수를 썼더니 시간초과가 나서 전체 합을 구하고 변화 할 때마다 빼고 더해주니 해결이 됬다.

### 배운점!
for 문 안에는 되도록 `sum()` 함수를 넣지 말자

## 코드
```python
def solution(queue1, queue2):
    ss = (sum(queue1) + sum(queue2)) // 2
    
    isBool = True
    
    a = 0
    q = queue1 + queue2
    s = 0
    e = len(queue1)
    sss = sum(q[s : e])
    
    while e < len(q):
        if ss == sss:
            break
        if ss > sss:
            sss += q[e]
            e += 1
        else:
            sss -= q[s]
            s += 1
        a += 1
        
    if e == len(q):
        isBool = False
        
    a1 = 0
    q = queue2 + queue1
    s = 0
    e = len(queue2)
    sss = sum(q[s : e])
    
    while e < len(q):
        if ss == sss:
            break
        if ss > sss:
            sss += q[e]
            e += 1
        else:
            sss -= q[s]
            s += 1
        a1 += 1    
        
    if  isBool == False and e == len(q):
        return -1
    
    elif isBool:
        return a
    
    return min(a, a1)
```

## 링크
https://school.programmers.co.kr/learn/courses/30/lessons/118667#