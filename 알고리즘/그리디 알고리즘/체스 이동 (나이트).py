"""
내가 한 풀이
order = input()
al = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
_y = order[0]
for i, v in enumerate(al):
    if v == _y:
        y = i + 1
x = int(order[1])

# 위에서 x,y 의 현재 위치를 만들었다.
print('현재 위치 : (', x, ',', y, ')')

# 이동 : [오른쪽2, 위1] , [오른쪽2, 아래1] , [왼쪽2, 위1] , [왼쪽2, 아래1]
#        [아래2, 왼쪽1] , [아래2, 오른쪽1] , [위2, 왼쪽1] , [위2, 오른쪽1]
result = 0
if y+2 < 8 and x-1 >0:
    result += 1
if y+2 < 8 and x+1 < 8:
    result += 1
if y-2 > 0 and x-1 > 0:
    result += 1
if y-2 > 0 and x+1 <8:
    result += 1
if y-1 > 0 and x+2 <8:
    result += 1
if y+1 < 8 and x+2 <8:
    result += 1
if y-1 > 0 and x-2 >0:
    result += 1
if y+1 < 8 and x-2 >0:
    result += 1
print(result)
"""

# 정답

input_data = input()
col = int(ord(input_data[0])) - int(ord('a')) + 1
row = int(input_data[1])
print('현재의 좌표 : (' + str(row) + ',' + str(col) + ')')
direction = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
result = 0
for d in direction:
    tmp_row = row + int(d[0])
    tmp_col = col + int(d[1])
    if 0 < tmp_row < 9 and 0 < tmp_col < 9:
        result += 1

print(result)
