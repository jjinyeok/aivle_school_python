# Q4 Answer Template
data = input('숫자로 이루어진 문자열을 입력하세요. ')

answer = max(int(data[0]) + int(data[1]), int(data[0]) * int(data[1]))
for i in range(2, len(data)):
    if data[i] == '0' or data[i] == '1':
        answer += int(data[i])
    else:
        answer *= int(data[i])

print(answer)
