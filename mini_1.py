# 미니실습 1

def max4(a, b, c, d):
    answer = a
    if b > answer:
        answer = b
    if c > answer:
        answer = c
    if d > answer:
        answer = d
    return answer


print('네 정수의 최댓값을 구합니다.')
a, b, c, d = map(int, input('정수 4개를 입력해주세요.: ').split())
answer = max4(a, b, c, d)
print(answer)
