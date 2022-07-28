# Q0 Answer template

def solution(a, b):
    tmp = min(a, b)
    while True:
        if a % tmp == 0 and b % tmp == 0:
            answer = tmp
            break
        tmp -= 1
    return answer


a, b = map(int, input('두 수를 입력하세요').split())
c = solution(a,b)
print(c)
