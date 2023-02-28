# 전력망을 둘로 나누기
## 코드
```python
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
def solution(n, wires):
    answer = 100
    
    for idx, wire in enumerate(wires):
        uf = [i for i in range(n + 1)]
        for i in range(len(wires)):
            if i == idx:
                continue
            union_parent(uf, wires[i][0], wires[i][1]) 
        s = {}
        sm = 0
        for j, u in enumerate(uf):
            if j == 0:
                continue
            if not u in s:
                s[u] = 1
            else:
                s[u] += 1
        if len(s.items()) == 2:
            vs = list(s.values())     
            answer = min(abs(vs[0] - vs[1]), answer)
    return answer
```