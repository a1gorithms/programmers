# 혼자 놀기의 달인

## 코드
```python
import itertools

def multiply(arr):
    result = 0
    for comb in itertools.combinations(arr, 2):
        result = max(comb[0] * comb[1], result)
    return result

def solution(cards):
    val = []
    for i in range(1, len(cards) + 1):
        if cards[i - 1] == -1:
            continue
        idx = i
        cnt = 0
        while cards[idx - 1] != -1:
            tmp = cards[idx - 1]
            cards[idx - 1] = -1
            idx = tmp
            cnt += 1
        if cnt != 0:
            val.append(cnt)
    if val and len(val) > 1:
        return multiply(val)
    else:
        return 0
```