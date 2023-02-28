# 거리두기 확인하기
## 설명

## 코드
```python
def solution(places):
    answer = []
    
    for place in places:
        chk = False
        for rn in range(5):
            if chk:
                break
            for cn in range(5):
                if (cn < 4) and place[rn][cn] == 'P' and (place[rn][cn + 1] == 'P'):
                    chk = True
                    break
                if rn < 4 and place[rn][cn] == 'P'and place[rn + 1][cn] == 'P':
                    chk = True
                    break
                if (cn < 4) and place[rn][cn] == 'P' and ((cn < 3 and place[rn][cn + 1] == 'O' and place[rn][cn + 2] == 'P')):
                    chk = True
                    break
                if (rn < 4) and place[rn][cn] == 'P' and (rn < 3 and place[rn + 1][cn] == 'O' and place[rn + 2][cn] == 'P'):
                    chk = True
                    break
                if (cn < 4 and rn < 4) and place[rn][cn] == 'P' and place[rn + 1][cn + 1] == 'P' and (place[rn][cn + 1] == 'O' or place[rn + 1][cn] == 'O'):
                    chk = True
                    break
                if (rn > 0 and cn < 4) and place[rn][cn] == 'P' and  place[rn - 1][cn + 1] == 'P' and (place[rn - 1][cn] == 'O' or place[rn][cn + 1] == 'O'):
                    chk = True
                    break
        if chk:
            answer.append(0)
        else:
            answer.append(1)
    return answer
```