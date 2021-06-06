# 집합 자료형  set
# 순서가 없고 중복을 허용하지 않음

# 초기화 방법 1
data1 = set([4, 18,21, 20, 55])
print("data1 : ", data1)

# 초기화 방법 2
data2 = {1, 65,32,3,34,24,4}
print("data2 : ",data2)

# 값 추가하기
data2.add(99)
print("data2 : ",data2)

data2.update([50, 90])
print("data2 : ",data2)

# 값 삭제하기
data2.remove(99)
print("remove 99! data2 : ",data2)

# 합집화(|), 교집합(&), 차집합(-)을 지원
print("합집합 : " ,data1 | data2)
print("교집합 : " ,data1 & data2)
print("차집합 : " ,data1 - data2)