# 완전 탐색
# n이 3이면 00시 00분 00초 ~ 03시 59분 59초내에 3이 포함되는 숫자를 모두 가져와라

n = int(input())
result = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                result += 1
    
print(result)
