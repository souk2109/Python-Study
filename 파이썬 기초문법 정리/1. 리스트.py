# ------ 리스트 -------
# 초기화
# 방법1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a[3] = 33
print(a)

# 방법2
b = [3] * 10
print(b)

# 슬라이싱
# index 번호가 3,4인 값을 가져옴
print(a[3:5])

# 리스트 컴플리헨션 (반복문으로 리스트 초기화)
# 2차원 배열 초기화 시 사용!!
arr = [i for i in range(10)]
# arr = [i for i in b] 도 가능
print(arr)

arr = [i*i for i in range(10) if i % 2 == 1]    # 0~9까지의 수 중 2로 나눴을 때 나머지가 1인 각각의 i값에 제곱을 한 값들을 리스트로 저장
print(arr)

# 리스트에 값 추가
arr.append(3)
print('after append 3 : ', arr)
arr.insert(4, 2)
print('after insert (4,2): ', arr)

# 오름차순
arr.sort()

# 내림차순
arr.sort(reverse=True)
print('after sort(reverse) : ', arr)

# 뒤집기
arr.reverse()
print('after reverse : ', arr)

print('arr.count(3) : ', arr.count(3))

arr.remove(3)
print('after remove 3 : ', arr)

# _ 반복을 위한 변수의 값을 무시할 때 _ 사용
for _ in range(3):
    print('출력')

# 리스트에서 모든 항목 삭제하기
remove_set = {1, 2}

target = [i for i in arr if i not in remove_set]
print(target)

[i for i in arr if i not in remove_set]
