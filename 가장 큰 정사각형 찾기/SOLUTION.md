# 가장 큰 정사각형 찾기

## 설명
처음 코드
```python
def solution(board):
    
    answer = 0
    mx = 0
    X = len(board)
    Y = len(board[0])
    if  X > Y:
        mx = Y
    else:
        mx = X
    i = mx
    while i >= 0:    
        chk = False
        for x in range(0, X - i):
            for y in range(0, Y - i):
                c = True
                for row in [board[xi][y:y + i + 1] for xi in range(x, x + i + 1)]:
                    if 0 in row:
                        c = c and False 
                if c:
                    chk = True
                    break
        if chk:
            return (i + 1) * (i + 1)
        i -= 1
    return answer
```

## 코드

```python
def solution(board):

    dp = [[0]* (len(board[0])+1) for _ in range(len(board)+1)]
    global_max = 0
    for i in range(1, len(board)+1):
        for j in range(1, len(board[0])+1):

            if board[i-1][j-1] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

                if dp[i][j] > global_max :
                    global_max = dp[i][j]


    return global_max**2
```