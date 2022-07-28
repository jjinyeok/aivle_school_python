# Q3 Answer template
import math

def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        sqrt_i = (math.sqrt(i))
        if sqrt_i == int(sqrt_i):
            answer -= i
        else:
            answer += i
    return answer

left = 13
right = 17
c = solution(left, right)
print(c)
