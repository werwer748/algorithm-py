"""
뒤집은 소수

N개의 자연수가 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 그 수를 출력하는 프로그램을 작성하세요.
예를 들어 32를 뒤집으면 23이고, 23은 소수이다. 그러면 23을 출력 한다.
단 910를 뒤집으면 19로 숫자화 해야 한다. 첫 자리부터의 연속된 0은 무시한다.
뒤집는 함수인 def reverse(x) 와 소수인지를 확인하는 함수 def isPrime(x)를 반드시 작성하여 프로그래밍 한다.
"""
import sys
sys.stdin = open('in5.txt', 'r')

n = int(input())
a = list(map(int, input().split()))


def reverse(x):
    n_to_s = str(x)
    new_string = ''
    for i in n_to_s:
        new_string = i + new_string
    return int(new_string)


def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return 0
    else:
        return 1

# reverse_list = list()
#
# for i in a:
#     reverse_list.append(reverse(i))
#
# for i in reverse_list:
#     if i > 1 and is_prime(i) == 1:
#         print(i, end=' ')
# print()
for x in a:
    tmp = reverse(x)
    if is_prime(tmp) == 1:
        print(tmp, end = ' ')
print()


"""
def reverse(x):
    res = 0
    while x > 0:
        t = x % 10 # 10으로 나눠서 한자리씩 떨어뜨린다
        res = res * 10 + t # 곱하면서 밀어낸다
        x = x // 10 # 10으로 나눈 몫을 계속 돌려준다 0 보다 작거나 같아질때까지

    return res


def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    else:
        return True


for x in a:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')
print()
"""