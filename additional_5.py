# Q5 Answer Template

n = input('숫자를 입력하세요. ')
len_n = len(n)
left, right = map(int, list(n[:len_n // 2])), map(int, list(n[len_n // 2:]))
if sum(left) == sum(right):
    print("LUCKY")
else:
    print("READY")
