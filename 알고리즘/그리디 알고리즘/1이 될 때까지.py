
n, k = list(map(int, input().split()))
print(str(n) + str(k))

# 25 3
# 내가 한 것
"""
count = 0
while n != 1:
    if n % k == 0:
        count += 1
        n = n / k

    else:
        n -= 1
        count += 1

print("count : ", count)

"""
count = 0
# 풀이
while True:
    # n에 가장 가까운 k의 배수
    target = (n//k) * k
    count += n-target
    n = target
    if n < k:
        break
    count += 1
    n = n//k
count += n-1

print(count)
