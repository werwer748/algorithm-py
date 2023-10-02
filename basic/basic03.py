'''
    조건문 if(분기, 중첩)
'''

'''
# x = 7
x = 5
if x != 7:  # == : 같다, != : 같지 않다
    print("Lucky")
    print("ㅋㅋㅋ")  # 들여쓰기(Indent) : 코드블럭 => 꼬이면 에러남 4칸 지키기
'''

'''
# 중첩 if
x = 12
if x > 10:
    if x % 2 == 1:
        print("10이상의 홀수")
        
x = 10
if x > 0:
    if x < 10:
        print("10보다 작은 자연수")
'''

'''
x = 7
if x > 0 and x < 10:
    print('10보다 작은 자연수')
x = 7
if 0 < x < 10:  # 이렇게하면 and 안써도됨. 파이썬만 가능
    print('10보다 작은 자연수')
'''

'''
x = -3
if x > 0:
    print("양수")
else:
    print("음수")
'''

'''
x = 50  # 하나의 문장 구조. 위에서부터 차례대로 실행하여 참이면 끝. 거짓이면 다음으로 넘어감
if x >= 90:
    print("A")
elif x >= 80:
    print("B")
elif x >= 70:
    print("C")
elif x >= 60:
    print("D")
else:
    print("F")
'''

x = 93  # 이렇게 쓰면 전부 출력 되어버림. 전부 다른 문장이 되는 것이다.
if x >= 90:
    print("A")
if x >= 80:
    print("B")
if x >= 70:
    print("C")
