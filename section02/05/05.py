"""
두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 가장
확률이 높은 숫자를 출력하는 프로그램을 작성하세요.
정답이 여러 개일 경우 오름차순으로 출력합니다.
"""
import sys
from collections import Counter

sys.stdin = open("in1.txt", "r")
n, m = map(int, input().split())

"""
a = []

for i in range(1, n + 1):
    for j in range(1, m + 1):
        a.append(i + j)

counter = dict(Counter(a))
counterMax = max(list(counter.values()))
setA = list(set(a))

res = []
# print(counterMax)
for x in setA:
    if counter[x] == counterMax:
        res.append(x)

res.sort()
print(res)
"""

cnt = [0] * (n + m + 3) # 눈의 최고합 이상은 안나오지만 여유 숫자 3을 더 줌
maxC = -2147000000

for i in range(1, n + 1):
    for j in range(1, m + 1):
        cnt[i + j] += 1

for i in range(n + m + 1):
    if cnt[i] > maxC:
        maxC = cnt[i]

for i in range(n + m + 1):
    if cnt[i] == maxC:
        print(i, end=' ')