# 변수는 데이터를 저장해 놓는 공간이다 라 이해하면 된다.
'''
    변수명 정하기
    1) 영문과 숫자, _로 이루어진다.
    2) 대소문자를 구분한다.
    3) 문자나, _로 시작한다.
    4) 특수문자를 사용하면 안된다. (&, % 등)
    5) 키워드를 사용하면 안된다. (if, for 등)
'''

a = 1
A = 2
A1 = 3
# 2b=4 error
print(a, A, A1)
a, b, c = 3, 2, 1
print(a, b, c)

# 값 교환
a, b = 10, 20
print(a, b)
a, b = b, a
print(a, b)

# 변수 타입
a = 12345123456123456123456  # 컴퓨터가 허용하는 범위까지 선언 가능
print(type(a))  # <class 'int'>
a = 12.123456789123456789
print(a)  # 8바이트까지만 표현
print(type(a))  # <class 'float'>
a = 'student'  # 홑따옴표 쌍따옴표 둘다 가능
print(a)  # student
print(type(a))  # <class 'str'>

# 출력방식
print("number")
a, b, c = 1, 2, 3
print(a, b, c)  # 1 2 3
print("number : ", a, b, c)  # number :  1 2 3
print(a, b, c, sep="")  # 123
print(a, b, c, sep=", ")  # 1, 2, 3
print(a, b, c, sep=",")  # 1,2,3
print(a, b, c, sep="\n")  # 1\n2\n3
# print는 기본적으로 출력 후 줄바꿈을 한다.
# 줄바꿈을 하지 않으려면 end 속성을 사용한다.
print(a, end=" ")
print(b, end=" ")
print(c)  # 1 2 3
