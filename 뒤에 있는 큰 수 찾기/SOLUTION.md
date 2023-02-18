# 뒤에 있는 큰 수 찾기
## 설명
바로 다음 수보다 큰 수는 스택에 넣어 판단을 보류하고 큰 수를 발견하면 스택에서 빼내어 비교한다.

## 코드 
```python
def solution(numbers):
    answer = [-1]*(len(numbers))
    stack = []
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    return answer
```