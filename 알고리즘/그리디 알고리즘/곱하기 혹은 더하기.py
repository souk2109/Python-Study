# 0 2 9 8 4 -> 0 + 2 * 9 * 8 * 4
# 현재 숫자가 0, 1이면 무조건 더하기
# 다음 숫자가 0, 1 이면 더하기 그 외는 곱하기

arr = input()
# 첫 번째 숫자
result = int(arr[0])
for i in range(1, len(arr)):
    num = int(arr[i])
    if num < 2 or result < 2:
        result += num
    else:
        result *= num
print(result)

"""
arr =  list(map(int, input().split()))
result = 0
for index, value in enumerate(arr):
    if value in [0, 1]:
        print("+", value, end=" ")
        result += value
    else:
        if result == 0 :
            print("+", value, end=" ")
            result += value
        else:
            print("*", value)
            result *= value

print(result)
"""