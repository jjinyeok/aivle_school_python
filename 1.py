# 실습 1

def electricPay(electric):
    if electric < 100:
        answer = 410 # 기본요금
        answer += electric * 60.7 # 전력량 요금
    elif 100 <= electric <= 200:
        answer = 910 # 기본요금
        answer += 60.7 * 100 + 125.9 * (electric - 100) # 전력량 요금
    else:
        answer = 1600 # 기본요금
        answer += 60.7 * 100 + 125.9 * 100 + 187.9 * (electric - 200) # 전력량 요금
    answer *= (1 + 0.1 + 0.037)
    return int(answer)


answer_250 = electricPay(250)
print(answer_250)
