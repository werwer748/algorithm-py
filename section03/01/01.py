"""
회문 문자열 검사

N개의 문자열 데이터를 입력받아 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우(회문 문자열) 이면 YES를 출력하고
회문 문자열이 아니면 NO를 출력하는 프로그램을 작성한다.
단 회문을 검사할 때 대소문자를 구분하지 않습니다.
"""
import sys
sys.stdin = open("in1.txt", "r")

n = int(input())

"""
# 내 풀이
for i in range(1, n + 1):
    ori = input().lower()
    rev = ''
    res = ''
    for v in ori:
        rev = v + rev

    if rev == ori:
        res = 'YES'
    else:
        res = 'NO'

    print("#%d %s" % (i, res))
"""

"""
# 강사 풀이
for i in range(n):
    s = input()
    s = s.upper()
    size = len(s)
    for j in range(size//2): # 대칭되는 글자만 비교하면 됨... ㄷㄷ
        if s[j] != s[-1-j]:
            print("#%d NO" % (i + 1))
            break
    else:
        print("#%d YES" % (i + 1))
"""
# 강사 풀이2
for i in range(n):
    s = input()
    s = s.upper()
    if s == s[::-1]: # [::-1] 문자열 리버스 시켜버림...
        print("#%d YES" % (i + 1))
    else:
        print("#%d NO" % (i + 1))