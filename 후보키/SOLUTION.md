# 후보키
## 설명


## 코드
```python
import itertools

def solution(relation):
    answer = 0
    tmp = []
    N = len(relation[0])
    cols = [i for i in range(N)]
    for i in range(1, N + 1):
        for col in itertools.combinations(cols, i):
            new_r = []
            for r in relation:
                arr = []
                for c in col:
                    arr.append(r[c])
                new_r.append(arr)
            uni = True
            mil = True
            buf = []
            for r in new_r:
                if r in buf:
                    uni = False
                    break
                buf.append(r)
                
            for t in tmp:
                # print(col , t)
                if set(t).issubset(col):
                    mil = False
                    break
                    
            if uni and mil:
                answer += 1
                tmp.append(col)
                
    return answer
```