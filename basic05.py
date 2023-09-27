'''
반복문을 이용한 문제풀이
 1) 1 ~ N까지 홀수 출력하기
 2) 1부터 N 까지의 합 구하기
 3) N의 약수 출력하기
'''

'''
n = int(input())
for i in range(1, n + 1):
    print(i)
'''

n = int(input())
'''
# 1번
for i in range(1, n + 1):
    if i % 2 == 1:
        print(i)
'''

'''
# 2번
sum = 0
for i in range(1, n + 1):
    sum = sum + i
print(sum)
'''

# 3번
for i in range(n, 0, -1):
    if n % i == 0:
        # print(i)
        print(i, end=' ')
