# 조이스틱

## 코드
```python
def solution(name):
    
    answer = 0
    n = len(name)
    
    for c in name:
        mn = 50
        mn = min(ord('Z') - ord(c) + 1, mn)
        mn = min(ord(c) - ord('A'), mn)
        answer += mn
    
    move = n - 1
    
    for idx in range(n):
        next_idx = idx + 1
        while (next_idx < n) and (name[next_idx] == 'A'):
            next_idx += 1
        distance = min(idx, n - next_idx)
        move = min(move, idx + n - next_idx + distance)

    answer += move
    
    return answer
```