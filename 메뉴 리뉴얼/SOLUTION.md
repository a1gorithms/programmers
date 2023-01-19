# 메뉴 리뉴얼
## 설명
손님의 주문 내역과 주방장이 코스로 만들고 싶은 요리의 개수가 주어진다.

손님의 주문 내역에서 많이 주문된 순서로 요리들을 골라 코스를 만든다. 

단, 많이 주문된 요리의 개수가 같을 때는 모두 출력한다.

## 코드
``` python
import itertools

def solution(orders, course):
    answer = []
    check = {}
    for c in course:
        for order in orders:
            for com in itertools.combinations(order, c):
                comb = "".join(sorted(list(com)))
                if  comb not in check:
                    check[comb]  = 1
                else:
                    check[comb] += 1
    for c in course:
        mx = 1
        maxV = []
        for k, v in check.items():
            if len(k) == c:
                # print(maxV)
                if int(v) > mx:
                    maxV = [k]
                    mx = int(v)
                elif int(v) == mx:
                    maxV.append(k)
                    
        if mx > 1:
            answer += maxV
    
    return sorted(answer)
```
## 링크
https://school.programmers.co.kr/learn/courses/30/lessons/72411