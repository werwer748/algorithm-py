'''
반복문(for, while)
'''
'''
# range는 인자로 들어온 숫자만큼의 크기를 갖는 리스트를 생성한다. 순차적으로 정수리스트를 생성한다.
# a = range(10)
a = range(-1, 11)  # 1~10까지의 리스트를 생성한다.
# a = range(-1.5, 11)  # 에러~! 정수만 가능하다.
print(a)  # range(0, 10) : 0부터 10미만의 숫자를 갖는 범위를 생성한다.
print(list(a))  # [1 ~ 9]의 리스트(array)로 변환한다.
'''

'''
for i in range(1, 11):
    # print('hello')
    print(i)
'''

'''
# for i in range(10, 0): # 아무일도 일어나지않음 ㅋㅋ
for i in range(10, 0, -2):  # 1씩 작아져라~
    print(i)
'''

'''
i = 1  # 변수에 값을 할당하고 시작해야 함
while i <= 10:
    print(i)
    i = i + 1
i = 10
while i >= 1:
    print(i)
    i = i - 1
'''

'''
i = 1
# while True:  # 무한루프 - true면 계속 도니까...
while i <= 10:
    print(i)
    # if i == 10:
    if i == 5:
        break  # while문을 빠져나간다.
    i += 1  # 연산자 축약
'''

'''
for i in range(1, 11):
    if i % 2 == 0:  # 짝수이면
        continue  # 아래 코드를 실행하지 않고 다음 반복으로 넘어간다.
    print(i)
'''

for i in range(1, 11):
    print(i)
    # if i == 5:
    #     break
    if i > 15:
        break
else:  # for문이 정상적으로 모두 실행되었을 때만 실행된다.
    print(11)
