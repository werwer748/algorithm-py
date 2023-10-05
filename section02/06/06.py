"""
자릿수의 합
N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력 하는 프로그램을 작성하세요.
각 자연수의 자릿수의 합을 구하는 함수를 def digit_sum(x)를 꼭 작성해서 프로그래밍 하세요
"""
import sys
sys.stdin = open("in2.txt", "r")

n = int(input())
a = list(map(int, input().split()))

"""
def digit_sum(x: int):
    split_sum = sum(list(map(int, list(str(x)))))
    return split_sum
"""
def digit_sum(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum


bigNum = 0
res = 0

for i, y in enumerate(a):
    if bigNum < digit_sum(y):
        bigNum = digit_sum(y)
        res = y

print(res)


"""
def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10 # 10씩 나눠서 나머지 구하면 자릿수가 나눠진다 ㄷㄷ 거기다 + 까지..
        x = x//10 # 최종적으로 한자리 남았을때는 몫이 0이 되니까 while이 멈춤
    return sum


max_sum = -2147000000
res = 0
for x in a:
    tot = digit_sum(x)
    if tot > max_sum:
        max_sum = tot
        res = x
print(res)
"""