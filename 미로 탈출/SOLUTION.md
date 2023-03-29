# 미로 탈출

## 코드
```python
from collections import deque
def solution(maps):
    answer = 0    
    R, C = len(maps), len(maps[0])
    q = deque()
    for idx, m in enumerate(maps):
        i = m.find("S")
        if i == -1:
            continue
        q.append((idx, i, 0))
    lever = False
    
    oprt = ((-1, 0), (0, -1), (1, 0), (0, 1))
    
    visited = set()
    
    while q:
        x, y, level = q.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if maps[x][y] == 'X':
            continue
        if lever and maps[x][y] == 'E':
            return level
        if not lever and maps[x][y] == 'L':
            lever = True
            q = deque()
            visited = set()
            visited.add((x, y))
        for i, j in oprt:
            if (0 <= x + i < R) and (0 <= y + j < C) and (x + i, y + j):
                q.append((x + i, y + j, level + 1))
    return -1
```
