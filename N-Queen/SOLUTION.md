# N-Queen

## 

## 시간초과 코드
```PYTHON
import itertools
def solution(n):
    answer = 0
    
    points = []
    
    
    for i in range(n):
        for j in range(n):
            points.append((i, j))
    if n == 12:
        for point in itertools.combinations(points, n // 2):
            boards = [ [0] * n for _ in range(n)]
            for idx, p in enumerate(point):
                boards[p[0]][p[1]] = idx + 1
            chk = False
            for idx, p in enumerate(point):
                if chk:
                    break
                for i in range(1, n + 1):
                    if chk:
                        break
                    for x, y in [(0, -i), (0, i), (i, 0), (-i, 0), (-i, i), (i, i), (i, -i), (-i, -i)]:
                        if (0 <= x + p[0]  and x + p[0] < n) and (0 <= y + p[1] and y + p[1] < n):
                            if boards[x + p[0]][y + p[1]] != 0:
                                chk = True
                                break
            if chk:
                continue
            answer += 1
        return answer * 2
       

    for point in itertools.combinations(points, n):
        boards = [ [0] * n for _ in range(n)]
        for idx, p in enumerate(point):
            boards[p[0]][p[1]] = idx + 1
        chk = False
        for idx, p in enumerate(point):
            if chk:
                break
            for i in range(1, n + 1):
                if chk:
                    break
                for x, y in [(0, -i), (0, i), (i, 0), (-i, 0), (-i, i), (i, i), (i, -i), (-i, -i)]:
                    if (0 <= x + p[0]  and x + p[0] < n) and (0 <= y + p[1] and y + p[1] < n):
                        if boards[x + p[0]][y + p[1]] != 0:
                            chk = True
                            break
        if chk:
            continue
        answer += 1
    return answer
```