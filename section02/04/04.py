"""
대표값
N명의 학생의 수학점수가 주어집니다.
N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고, N명의 학생 중 평균에 가장 가까운 학생은
몇 번째 학생인지 출력하는 프로그램을 작성하세요.
평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호를 답으로 하고,
높은 점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 빠른 학생의 번호를 답으로 합니다.
"""
import sys
sys.stdin = open("in2.txt", "rt")
"""
s_ea = int(input())
points = list(map(int, input().split()))

ave = round(sum(points) / s_ea)

# print(eve)
m = abs(ave - points[0])
idx = 0

for i in range(1, len(points)):
    if m > abs(ave - points[i]):
            m = abs(ave - points[i])
            idx = i

print(ave, idx + 1)
"""
"""
round의 오류
파이썬에서 round는 round_half_up (4 이하면 버리고 5 이상이면 올림) 이 아니고
round_half_even(a=4.500이라고 하면 5가 나와야하는데 4가 나옴 짝수쪽으로 간다고?
아무튼 정확하지 않다. 1의 자리가 짝수면 버려버린다는건가) 방식이라고 함
그래서 해결 방법은?
소숫점에 0.5를 더하고 int()로 감싸면 소숫점 떨어진다
"""
n = int(input())
a = list(map(int, input().split()))
# ave = round(sum(a) / n)
ave = int((sum(a) / n) + 0.5)
mini = float("inf")
score = 0
res = 0

for idx, x in enumerate(a):
    tmp = abs(x - ave)
    if tmp < mini:
        mini = tmp
        score = x
        res = idx + 1
    elif tmp == mini:
        if x > score:
            score = x
            res = idx + 1

print(ave, res)