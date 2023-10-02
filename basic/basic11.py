'''
함수 만들기
'''
# def 디파인이라고 읽는다. def 함수명 이런식으로 쓴다. 선언하고 호출해야한다.

'''
# 기본적인 함수 사용법
def add(a, b):
    c = a + b
    print(c)


add(3, 2)
add(5, 7)
'''

'''
# return 사용법
def add(a, b):
    c = a + b
    return c


x = add(3, 2)
print(x)
'''

'''
# 여러개의 값 리턴하기
def add(a, b):
    c = a + b
    d = a - b
    return c, d  # 튜플 형태로 반환


print(add(3, 2))
'''


def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


a = [12, 13, 7, 9, 19]

for y in a:
    if isPrime(y):
        print(y, end=' ')
print()
