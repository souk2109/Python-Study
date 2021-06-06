# 딕셔너리(사전)
# 해쉬 테이블을 사용하므로 O(1)의 시간만 소요
# 키와 값으로 구성
# 키는 변경이 불가능한 튜플, 문자를 이용

# 초기화
data = dict()
print(data)

# 값 넣기 1
data['사과'] = 'apple'
data['오렌지'] = 'orange'
print("data : ",data)
keys = data.keys()
for key in keys:
    if key == '사과':
        print('사과 있음')

# 값 넣기 2 (json 형식으로 넣기)
data2 = dict()
data2 = {
    'kim': 98,
    'jin': 22
}
print("data2 : ", data2)
print("data2.keys() : ", data2.keys())  # 반환형은 dict_keys 이므로 리스트로 형 변환이 필요함
print("list(data2.keys()) : ", list(data2.keys()))  # 형 변환
print("data2.values() : ", list(data2.values()))

