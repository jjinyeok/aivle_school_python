# Q2 Answer template

n = int(input())
count = 0
tmp = n * 1
while True:
    if count != 0 and tmp == n:
        break
    left, right = tmp // 10, tmp % 10
    sum_left_right = left + right
    sum_left, sum_right = sum_left_right // 10, sum_left_right % 10
    tmp = right * 10 + sum_right
    count += 1
print(count)
