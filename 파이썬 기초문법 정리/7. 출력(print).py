# -------------- print --------------
# print 후 띄어쓰기 못하게 하려면 end 사용
print('hello', end=" ")
print('hello')

# 문자열 이어 쓰기
print('hello' + 'kim')

# 문자열과 숫자 이어쓰기 -> 숫자는 str로 형 변환 후 사용
print('hello' + str(3) + 'kim')

# ----------------- 기본적이지만 기억할 것 -------------------------------------

# if문 참고! if, elif, else 이렇게 3가지로 나뉨
# 논리 연산에 !가 없음 -> and or not 사용
a = 550
if a < 50 and a > 0:
    print('참')

# 아래도 가능..!
if 0 < a < 50:
    print('참')

# 참 거짓은 Ture, False로 표시!

# in, not in 연산자는 다수의 데이터를 담는 자료형을 위해 제공된다.
# 리스트, 튜플, 문자열, 딕셔너리 모두 사용 가능

# if문에서 로직을 작성하지 않고 pass를 사용해서 넘어갈 수 있다.
if a > 50:
    pass
elif a > 30:
    print('pass')
