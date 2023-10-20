"""
수들의 합

N개의 수로 된 수열 A[1], A[2], ..., A[N] 이 있다.
이 수열의 i번째 수부터 j번째 수까지의 합 A[i]+A[i+1]+...+A[j-1]+A[j]가 M이 되는 경우의 수를 구하는
프로그램을 작성하시오.
"""
import sys
sys.stdin = open('test.txt', 'r')

# 강사 풀이
n, m = map(int, input().split())
a = list(map(int, input().split()))
lt = 0
rt = 1
tot = a[0]
cnt = 0

while True:
    if tot < m: # 4 < 5
        if rt < n: # 3 < 10
            tot += a[rt] # 4 + 1
            rt += 1 # 4
        else:
            break
    elif tot == m: # 5
        cnt += 1 # 2
        tot -= a[lt] # 5 - 2
        lt += 1 # 1
    else:
        tot -= a[lt]
        lt += 1
print(cnt)

"""
# 내 풀이
n, m = map(int, input().split())
a = list(map(int, input().split()))

cnt = 0
rt = 1
for i in range(n):
    tot = a[i]
    if rt < n:
        for j in range(rt, n):
            tot += a[j]
            if tot == m:
                cnt += 1
        rt += 1
print(cnt)
"""

