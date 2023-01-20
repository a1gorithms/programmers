# [3차] 방금그곡
## 설명
#이 붙은 음표가 있으므로 변환을 해주던가 리스트에 따로 묶는다.

시간에 비례한 악보를 정확하게 맞춰줘야하는게 포인트다.
## 코드

``` python
def solution(m, musicinfos):
    answer = []
    def convert(s):
        output = []
        for c in s:
            if c.isalpha():
                output.append(c)
            else:
                output[-1] = output[-1] + c
        return output
    cm = convert(m)
        
    for musicinfo in musicinfos:
        time1, time2, name, sound = musicinfo.split(',')
        time1H, time1M = map(int, time1.split(':'))
        time2H, time2M = map(int, time2.split(':'))
        time = (time2M - time1M + (time2H - time1H) * 60)
        cs = convert(sound)
        if time >= len(cs):
            md = (time % len(cs))
            cs *= (time // (len(cs)))
            cs = cs + cs[:md]
            print(cs)
        else:
            cs = cs[:time]
        for i in range(len(cs)):
            if len(cm) == len(cs[i : i + len(cm)]) and cm == cs[i : i + len(cm)]:
                answer.append((name, time))
        
    if answer:
        answer.sort(key=lambda x : x[1], reverse=True)
        return answer[0][0]
    
    return "(None)"
```
## 링크
https://school.programmers.co.kr/learn/courses/30/lessons/17683#