# 파이썬의 내장 함수와 기본 라이브러리 사용법
# 내장함수의 경우 튜플, 리스트에 모두 적용 가능하다.
sumTuple = sum((1, 2, 3, 4))
sumList = sum([1, 2, 3, 4])
print("sumTuple : ", sumTuple)
print("sumList : ", sumList)

minTuple = min((6, 3, 10, 4))
minList = min([21, 5, 1, 9])
print("minTuple : ", minTuple)
print("minList : ", minList)

maxTuple = max((6, 3, 10, 4))
print("maxTuple : ", maxTuple)
maxList = max([21, 5, 1, 9])
print("maxList : ", maxList)

# 문자열의 수식을 계산해줌
result = eval("(3+5)*2")
print(result)

# 정렬 내장 함수 sorted
array = [('홍길동', 20), ('홍길준', 55), ('홍길남', 24), ('홍길순', 13)]
result = sorted(array, key=lambda x: x[1], reverse=True)
print(result)

# 외부 함수
from itertools import permutations
from itertools import product
from itertools import combinations
from itertools import combinations_with_replacement

data = ['A', 'B', 'C']

# 순열
result = list(permutations(data, 2))
print(result)

# 조합
result = list(combinations(data, 2))
print(result)

# 중복 순열 (자신을 포함)
result = list(product(data, repeat=2))
print(result)

# 중복 조합 (자신을 포함)
result = list(combinations_with_replacement(data, 2))
print(result)

from collections import Counter

counter = Counter(['red', 'red', 'red', 'blue'])
print(counter)
print(counter['blue'])

# 최대 공약수, 최소 공배수(LCM, Least Common Multiple) 구할 때 유용
# 최소 공배수는 두 수의 곱에서 최대 공약수를 나눠주면 됨
import math

print(math.gcd(21, 14))


def find_lcm(a, b):
    return a * b / math.gcd(a, b)


lcm = find_lcm(3, 4)
print(lcm)
