# 미니실습 2

def waterPay(company, usage):
    if company == 'A':
        answer = usage * 100
    elif company == 'B':
        if usage <= 50:
            answer = usage * 150
        else:
            answer = usage * 75
    return answer


company, usage = input("수도회사와 수도 사용량을 입력해주세요: ").split()
answer = waterPay(company, int(usage))
print(answer)
