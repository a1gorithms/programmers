# 다리를 지나는 트럭
## 접근 방식
쳐음에는 문제가 잘 이해가 안되서 출처에 있는 원본 문제를 보고 이해가 됬다.

매초마다 그 상황을 만들어 구분하면 될 거라고 생각했다.

그래서 다리 길이 만큼의 `큐`를 만들어 매초 deque 하고 다리 위에 더 올라 올 수 있으면 enque 해서 모든 트럭이 다리를 지나가면 그때의 시간을 반환한다.

근데 처음에 생각한 코드로 풀면 문제가 생기는데 5번 테스트 케이스에서 시간초과가 난다.

for 문안에 sum()이 있어서 그렇다고 한다. 

그래서 enque deque 때 값을 더하고 빼주면서 계속 들고 가면 된다.
## 처음 생각한 코드
```python
def solution(bridge_length, weight, truck_weights):
    answer = 0
    i = 0
    bd = [0] * bridge_length
    while True:
        if len(truck_weights) == 0:
            if sum(bd) == 0:
                return i
            else:
                return i + len(bd)
        bd.pop(0)
        if len(bd) + 1 <= bridge_length and weight >=  sum(bd) + truck_weights[0]: // 여기
            bd.append(truck_weights[0])
            truck_weights = truck_weights[1:]
        else:
            bd.append(0)
        i += 1
```
## 링크
https://school.programmers.co.kr/learn/courses/30/lessons/42583?language=python3