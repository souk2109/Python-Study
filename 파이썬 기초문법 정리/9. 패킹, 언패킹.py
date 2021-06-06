# 파이썬은 함수에서 여러 개의 값을 리턴할 수 있다.
# 이 과정을 패킹이라하고 값을 꺼낼 때 언패킹이라고 한다.

def calcul(num1, num2):
    add_result = num1 + num2
    minus_result = num1 - num2
    mul_result = num1 * num2
    div_result = num1 / num2
    return add_result, minus_result, mul_result, div_result


add_result, minus_result, _, div_result = calcul(8, 3)

print(add_result, minus_result, _, div_result)
