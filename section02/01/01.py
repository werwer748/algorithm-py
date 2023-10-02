'''
K 번째 약수
'''
import sys
sys.stdin = open("in2.txt", "rt")
'''
# 내 풀이
n = input()
number = int(n.split()[0])
th = int(n.split()[1])

numbers = []

for i in range(1, number + 1):
    if number % i == 0:
        numbers.append(i)

numbers.sort()
# print(numbers)
if len(numbers) >= th :
    print(numbers[th - 1])
else:
    print(-1)
'''

# 강사 풀이
n, k = map(int, input().split())
# print(n, k)
cnt = 0
for i in range(1, n + 1):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else:
    print(-1)