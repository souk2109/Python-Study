# 전역변수인 num을 함수에서 사용하기 위해서 global를 사용
num = 1
def add():
    # global num += 1 은 에러!
    global num
    num += 1
    return num

for i in range(1,10):
    add()
print(num)

# list의 경우에는 함수내에서 global없이 전역변수 사용이 가능하다.
array = [1, 3, 2, 4, 10]
def appendToArray():
    array.append(12)
    print(array)
    
appendToArray()
