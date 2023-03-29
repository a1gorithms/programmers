# 테이블 해시 함수

## 코드
```python
def solution(data, col, row_begin, row_end):
    answer = 0
    buf = []
    data.sort(key=lambda x : x[0], reverse=True)
    data.sort(key=lambda x : x[col - 1])
    
    for i in range(row_begin - 1, row_end):
        buf.append(data[i])
        
    si = []
    for bs, i in zip(buf, range(row_begin, row_end + 1)):
        si.append(sum([b % i for b in bs]))
    
    f = si[0]
    if len(si) == 1:
        return si[0]
    
    for i in range(1, len(si)):
        f = f ^ si[i]
    
    return f
```