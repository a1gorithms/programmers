# 무인도 여행
## 설명

## 코드
```python
from collections import deque
def solution(maps):
    N, M = len(maps), len(maps[0])
    visited = [[0]*M for _ in range(N)]

    answer = []
    for i in range(N):
        for j in range(M):
            if maps[i][j]=='X' or visited[i][j]:
                continue
            queue = deque()
            queue.append((i,j))
            visited[i][j]=1
            n_food = int(maps[i][j])
            while queue:
                i0, j0 = queue.popleft()
                for di, dj in [(1,0), (0,1), (-1,0), (0,-1)]:
                    ni, nj = i0+di, j0+dj
                    if 0<=ni<N and 0<=nj<M and not visited[ni][nj] and maps[ni][nj]!='X':
                        queue.append((ni,nj))
                        visited[ni][nj] = 1
                        n_food += int(maps[ni][nj])
            answer.append(n_food)
    if not answer:
        answer.append(-1)
    else:
        answer.sort()
    return answer
```
```python
import sys

print(sys.setrecursionlimit(10000))


def solution(maps):
    maps = [list(map(str, i)) for i in maps]
    answer = []
    cl = len(maps[0])
    rl = len(maps)
    oprts = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def bfs(x, y, value):
        if x >= cl or y >= rl or x < 0 or y < 0:
            return value
        if maps[y][x] == "X":
            return value
        value += int(maps[y][x])
        maps[y][x] = "X"
        for xi, yi in oprts:
            value = bfs(x + xi, y + yi, value)
        return int(value)
    
    for i in range(rl):
        for j in range(cl):
            if maps[i][j] == "X":
                continue
            else:
                answer.append(bfs(j, i, 0))

    return sorted(answer) if answer else [-1]
```