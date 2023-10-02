"""
K번째 수
"""
import sys
sys.stdin = open('in5.txt', 'rt')
"""
input 가져올 때 마다 한줄씩 짤려서 들어옴... 
print(input())
print(input())
print(input())
print(input())
print(input())
"""
T = int(input())
print(T)
for t in range(T):
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    a_split = a[s - 1:e]
    a_split.sort()
    # print("#" + str(t + 1), a_split[k - 1])
    print("#%d %d" % (t + 1, a_split[k - 1]))
