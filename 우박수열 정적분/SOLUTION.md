# 우박수열 정적분
## 설명
평행사변형의 넓이를 미리 구해놔서 주어진 범위만큼 합을 구하면 됨.

## 코드
```python
def solution(k, ranges):
    answer = []
    
    a = [k]
    
    while k > 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = k * 3 + 1
        a.append(k)
    b = []
    for i in range(len(a) - 1):
        b.append((a[i] + a[i + 1]) / 2)
    for rng in ranges:
        if rng[0] > len(b) + rng[1]:
            answer.append(-1)
        else:
            answer.append(sum(b[rng[0]: len(b) + rng[1]]))
    return answer
```