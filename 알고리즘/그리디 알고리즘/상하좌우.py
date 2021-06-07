"""
내가 작성한 코드

n = int(input())
arr = list(map(str, input().split()))
print(arr)

# 2차원 배열 구조
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print("(" + str(i) + ", " + str(j) + ")", end=" ")
    print("")


# 현재 X방향
c_x = 1
# 현재 Y방향
c_y = 1
for k in arr:
    if k == 'R':
        if c_y == 5:
            continue
        c_y += 1
    if k == 'U':
        if c_x == 1:
            continue
        c_x -= 1
    if k == 'D':
        if c_x == 5:
            continue
        c_x += 1
    if k == 'L':
        if c_y == 1:
            continue
        c_y -= 1
print("("+str(c_x) + ", "+str(c_y) + ")", end=" ")

"""
# 정답 코드
n = int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print("(" + str(i) + ", " + str(j) + ")", end=" ")
    print("")

plans = list(map(str, input().split()))
x, y = 1, 1
# L R U D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            if nx > n or ny > n or nx <1 or ny < 1:
                continue
            x = nx
            y = ny
print("(" + str(x) + "," + str(y) + ")")