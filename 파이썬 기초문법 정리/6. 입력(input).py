# --------------input --------------
# 정수를 입력받음
import sys

n = int(input())
# 1. 데이터를 입력받는데 공백을 기준으로 리스트 형태로 저장
# 2. map을 이용해 int로 변환 후 list로 저장
data = list(map(int, input().split()))
print(n)
print(data)

# 입력 수 가 정해진 경우 (4개 입력 시 에러)
n, m, k = map(int, input().split())


# 입력을 최대한 빠르게 받기 위한 코드
sinput = sys.stdin.readline().rstrip()
print(list(map(int, sinput.split())))