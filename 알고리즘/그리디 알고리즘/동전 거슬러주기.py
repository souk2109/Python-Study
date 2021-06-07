# 1260원을 500, 100, 50, 10원의 동전으로 거슬러 줄 때 최소한의 동전을 사용한다.
# 거슬러줘야 할 동전의 수는?

money = 1260
money_arr = [500, 100, 50, 10]
count = 0
for i in money_arr:
    count += money // i
    money %= i

print(count)