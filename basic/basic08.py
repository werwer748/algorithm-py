'''
리스트와 내장함수(1)
'''

import random as r

# a = []
# print(a)
# b = list()
# print(b)

a = [1, 2, 3, 4, 5]
# print(a)
# print(a[0])  # 1

b = list(range(1, 11))
# print(b)

c = b + a  # 순서대로 붙음
# print(c)

print(a)
a.append(6)  # 맨 뒤에 추가
print(a)

a.insert(3, 7)  # 3번째 index에 7을 추가
print(a)

a.pop()  # 맨 뒤에 있는 것을 빼냄
print(a)
a.pop(3)  # 3번째 index를 빼냄
print(a)

a.remove(4)  # 4를 찾아서 지움
print(a)

print(a.index(5))  # 5의 index를 알려줌

a = list(range(1, 11))
print(a)
print(sum(a))  # 리스트 내 모든 값의 합
print(max(a))  # 리스트 내 최대값
print(min(a))  # 리스트 내 최소값 - 인자들 중에 최소값을 찾는거임
print(a)

r.shuffle(a)  # 리스트 내의 값들을 랜덤하게 섞어줌
print(a)

a.sort(reverse=True)  # 리스트 내의 값들을 내림차순으로 정렬
print(a)

a.sort()  # 리스트 내의 값들을 오름차순으로 정렬
print(a)

a.clear()  # 리스트 내의 모든 값을 지움
print(a)
