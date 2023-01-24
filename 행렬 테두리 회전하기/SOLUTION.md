# 행렬 테두리 회전하기
## 설명
리스트에 변경되는 범위의 숫자들을 넣고
첫 번째 숫자보다 한 칸 앞에 부터 시작해서 리스트 있는 숫자들을 pop 해주면 된다.

## 코드
``` python
def solution(rows, columns, queries):
    answer = []
    mat = []
    index = 1
    
    for r in range(rows):
        row = []
        for c in range(columns):
            row.append(index)
            index += 1
        mat.append(row)
    
    for q in queries:
        x1, y1, x2, y2 = map(lambda x : x - 1, q)
        buf = []
        
        for i in range(y2 - y1 + 1):
            buf.append(mat[x1][y1 + i])
        
        for i in range(1, x2 - x1 + 1):
            buf.append(mat[x1 + i][y2])
        
        for i in range(1, y2 - y1 + 1):
            buf.append(mat[x2][y2 - i])
        
        for i in range(1, x2 - x1):
            buf.append(mat[x2 - i][y1])
        
        answer.append(min(buf))
        
        for i in range(1, y2 - y1):
            mat[x1][y1 + i] = buf.pop(0)
        
        for i in range(x2 - x1):
            mat[x1 + i][y2] = buf.pop(0)
        
        for i in range(y2 - y1):
            mat[x2][y2 - i] = buf.pop(0)
        
        for i in range(x2 - x1 + 1):
            mat[x2 - i][y1] = buf.pop(0)
        
    return (answer)
```

## 링크
https://school.programmers.co.kr/learn/courses/30/lessons/77485#