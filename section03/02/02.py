"""
숫자만 추출

문자와 숫자가 섞여있는 문자열이 주어지면 그 중 숫자만 추출하여 그 순서대로 자연수를 만 듭니다.
만들어진 자연수와 그 자연수의 약수 개수를 출력합니다.
만약 “t0e0a1c2h0er”에서 숫자만 추출하면 0, 0, 1, 2, 0이고 이것을 자연수를 만들면 120이 됩니다.
즉 첫자리 0 은 자연수화할 때 무시 합니다. 출력은120를 출력하고,다음 줄에120 의 약수의 개수를 출력하면 됩니다.
추출하여 만들어지는 자연수는 100,000,000을 넘지 않습니다.
"""
import re
import sys
sys.stdin = open('in1.txt', 'r')

# 강사 풀이
s = input()
res = 0

for x in s:
    # isdecimal: 0~9 까지의 숫자만 찾아 줌
    # isdigit: 숫자 형태로 들어오는 것들까지 찾아준다 2의 제곱이라던가..
    if x.isdecimal():
        res = res * 10 + int(x)
print(res)

cnt = 0
for i in range(1, res + 1):
    if res % i == 0:
        cnt += 1
print(cnt)


"""
#까먹지 마랒...
test = 1234
rev = 0

while test > 0:
    t = test % 10
    rev = rev * 10 + t
    test = test//10

print(rev)
"""
"""
# 내 풀이
nums = re.sub(r'[^0-9]', '', input())
n = int(nums)
cnt = 0

for i in range(1, n + 1):
    if n % i == 0:
        cnt += 1

print(n, cnt, sep='\n')
"""