# 호텔 대실
## 설명

## 코드
```python
def solution(book_time):
    answer = 0
    rooms = []
    book_time.sort(key=lambda x : x[0])
    book_time = [(int(s[:2]) * 60 + int(s[3:]), int(e[:2]) * 60 + int(e[3:])) for s, e in book_time]
    for s, e in book_time:
        if not rooms:
            rooms.append([(s, e)])
            continue
        isClear = False
        for i in range(len(rooms)):
            if rooms[i][-1][1] + 10 <= s:
                rooms[i].append((s, e))
                isClear = True
                break
        if not isClear:
            rooms.append([(s, e)])
    
    return len(rooms)
```