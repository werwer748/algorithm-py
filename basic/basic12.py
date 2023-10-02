'''
람다 함수?
- 이름이 없는 함수, 익명 함수, 람다 표현식이라고도 한다.
'''

'''
def plus_one(x):
    return x + 1


print(plus_one(1))
'''

'''
def plus_two(x): return x + 2  # 람다 함수는 이름이 없기 때문에 변수에 할당해야한다.
print(plus_two(1))
'''


def plus_one(x):
    return x + 1


a = [1, 2, 3]
# 함수 선언 방법에 따른 사용법의 차이
print(list(map(plus_one, a)))
print(list(map(lambda x: x + 10, a)))
