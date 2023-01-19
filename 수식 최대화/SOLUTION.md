# 수식 최대화

## 접근 법
숫자와 수식을 리스트에 넣는다.

그리고 연산자의 우선순위를 정한다.

가장 큰 수를 출력한다.


## 코드
``` python
import itertools

def solution(expression):
    exps = []
    buf = []
    for exp in list(expression):
        if not exp.isdigit():
            exps.append("".join(buf))
            buf = []
            exps.append(exp)
            continue
        buf.append(exp)
    exps.append("".join(buf))
    optrs = ['*', '-', '+']
    answer = 0
    
    for p in itertools.permutations(optrs, 3):
        cexps = exps[:]
        for op in list(p):
            while op in cexps:
                index = cexps.index(op)
                cexps.pop(index)
                if op == '*':
                    cexps.insert(index - 1, int(cexps.pop(index - 1)) * int(cexps.pop(index - 1)))
                elif op == '-':
                    cexps.insert(index - 1, int(cexps.pop(index - 1)) - int(cexps.pop(index - 1)))
                else:
                    cexps.insert(index - 1, int(cexps.pop(index - 1)) + int(cexps.pop(index - 1)))
        
        answer = max(answer, abs(int(cexps[0])))
    
    return answer
```

## 링크
https://school.programmers.co.kr/learn/courses/30/lessons/67257