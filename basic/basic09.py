'''
리스트와 내장함수 (2)
'''
a = [23, 12, 36, 53, 19]
print(a[:3])
print(a[1:4])
print(len(a))

for i in range(len(a)):
    print(a[i], end=' ')
print()

for x in a:
    print(x, end=' ')
print()

for x in a:
    if x % 2 == 1:
        print(x, end=' ')
print()

for x in enumerate(a):  # enumerate : 인덱스와 값을 함께 출력
    print(x)  # 튜플 형태로 출력됨

b = (1, 2, 3, 4, 5)  # 튜플
print(b[0])
# b[0] = 7  # 튜플은 수정이 안됨
# print(b)

for x in enumerate(a):
    print(x[0], x[1])
print()

for index, value in enumerate(a):
    print(index, value)
print()

if all(60 > x for x in a):  # all : 모든 값이 참이면 참
    # if all(10 < x < 60 for x in a):
    print("YES")
else:
    print("NO")

if any(11 > x for x in a):  # any : 하나라도 참이면 참
    print("YES")
else:
    print("NO")
