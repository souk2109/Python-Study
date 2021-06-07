# 안보고 다시 푼 답안
n = int(input())
plans = list(map(str, input().split()))

# 현재 위치
x = 1
y = 1
# LRUD
d_x = [0, 0, -1, 1]
d_y = [-1, 1, 0, 0]

directs = ['L', 'R', 'U', 'D']

for i in plans:
    for index, k in enumerate(directs):
        if k == i:
            temp_x = x + d_x[index]
            temp_y = y + d_y[index]
            if 0 < temp_x < n + 1 and 0 < temp_y < n + 1:
                x = temp_x
                y = temp_y
print("(", x, ",", y, ")")
