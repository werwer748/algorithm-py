# 변수입력과 연산자

'''
a = input("숫자를 입력하세요 : ")
print(a)
'''

'''
a, b = input("숫자를 입력하세요 : ").split()  # split()은 공백을 기준으로 나눈다.
print(type(a))
a = int(a)  # 문자열을 숫자로 변환
b = int(b)
print(type(a))
# print(type(c))  # 문자열로 인식해서 붙여서 출력
print(a + b)
'''

'''
a, b = map(int, input("숫자를 입력하세요 : ").split())
# map(변환함수, 입력값) : 입력값을 변환함수로 변환
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)  # 몫
print(a % b)  # 나머지
print(a ** b)  # 제곱
'''

a = 4.5
b = 5
c = a + b
print(c)
print(type(c))  # 실수 > 정수 따라서 <class 'float'>
