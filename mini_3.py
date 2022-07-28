# 미니 실습 3

def loop(a, b):
    if a > b:
        a, b = b, a
    sum = b
    for i in range(a, b):
        print(f'{i} + ', end='')
        sum += i
    print(f'{b} = {sum}')


a, b = map(int, input('두 정수를 입력해주세요: ').split())
loop(a, b)
