"""
# 내가 푼 풀이
input_data = input()
data = sorted(input_data)
sum = 0
result = ''
for i in data:
    # 숫자인 경우
    if int(ord('0')) <= int(ord(i)) <= int(ord('9')):
        sum += int(i)
    else:
        result += i

print(result+str(sum))
"""

# 정답
data = input()
sum = 0
alpha_list = []
for i in data:
    if i.isalpha():
        alpha_list.append(i)
    else:
        sum += int(i)
alpha_list.sort()
alpha_list.append(str(sum))
print(''.join(alpha_list))