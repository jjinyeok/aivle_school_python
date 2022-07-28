# Q1 Answer template

def solution(a, b):
    tmp = max(a, b)
    while True:
        if tmp % a == 0 and tmp % b == 0:
            answer = tmp
            break
        tmp += 1
    return answer


a, b = map(int, input('두 수를 입력하세요').split())
c = solution(a,b)
print(c)
