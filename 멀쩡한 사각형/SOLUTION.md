# 멀쩡한 사각형
## 설명
## 코드
```python
import math

def solution(w,h):
    return (w*h)-(w+h-math.gcd(w,h))
```