# 미니 실습 4

def find_rectangle_length(area):
    for i in range(1, area + 1):
        if area % i == 0:
            print(f'{i} * {area // i}')


area = int(input('직사각형의 넓이를 입력하세요.:'))
find_rectangle_length(area)
