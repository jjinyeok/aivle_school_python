# 실습 2

def solution(n):
    answer = ''
    i = 0
    while i != n:
        if i % 2 == 0:
            answer += '+'
        else:
            answer += '-'
        i += 1
    return answer


print('+ 와 -를 번갈아 출력합니다.')
n = int(input('몇 개를 출력할까요? '))
answer = solution(n)
print(answer)
