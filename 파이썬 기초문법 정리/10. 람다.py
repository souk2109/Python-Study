# 람다 함수로 간편하게 함수를 작성할 수 있다.
# 한 번만 사용 할 함수가 있는 경우 사용한다.

array = [('kim', 50), ('jang', 20), ('kin', 40), ('dme', 80)]
print(sorted(array, key=lambda x: x[1]))


list1 = [1, 4, 2, 3, 1]
list2 = [2, 1, 3, 4, 2]

print(list(map(lambda x, y: x+y, list1, list2)))

