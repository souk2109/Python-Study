# 파이썬의 간편한 if문
a = 40
if a < 80: print('80보다 작습니다.')

# 파이썬의 3항 연산자
result = 'success' if a > 30 else 'fail'
print(result)

result = 0
for k in range(1, 10):
    if k % 2 == 1:
        result += k
    k += 1

print(result)
