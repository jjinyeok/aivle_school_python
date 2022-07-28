# 실습 4
import math

def find_root_pwr(n):
    root = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        for pwr in range(2, 6):
            if i ** pwr == n:
                root = i
                break
    return root, pwr


n = int(input('정수를 입력하세요: '))
root, pwr = find_root_pwr(n)
if root == 0:
    print('결과 없음')
else:
    print(f'root: {root}, pwr: {pwr}')
