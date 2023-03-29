# 덧칠하기
## 설명
뒤에서 부터 본다.
칠하고 있는 포인터와 순회하는 포인터를 두고, 칠하고 있는 포인터와 순회하는 포인터가 같을 때는 페인트 칠을 시작하는 부분이기 때문에 answer 을 1 올려주고 그렇지 않을 때는 이미 칠해지고 있는 상태이다.

그때 칠해지는 범위 안에 있으면 continue 후 순회를 계속하며 범위 밖으로 나간 경우 answer 을 1 올려준다.

그 결과가 정답이다.
## 코드
```python
def solution(n, m, section):
    answer = 0
    section.sort(reverse=True)
    idx = 0
    for i in range(0, len(section)):
        if idx == i:
            answer += 1
        else:
            if section[i] > section[idx] - m:
                continue
            else:
                answer += 1
                idx = i
    
    return answer
```