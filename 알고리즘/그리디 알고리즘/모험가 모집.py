arr = list(map(int, input().split()))
arr = sorted(arr)
result = 0
count = 0
for i in arr:
    count += 1
    if i <= count:
        print(str(i) + "에서 출력")
        result += 1
        count = 0

print("결과 : " , result)

