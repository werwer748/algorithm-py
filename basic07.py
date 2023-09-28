'''
문자열과 내장함수
'''

msg = "It is Time"
print(msg.upper())  # 대문자로 변환
print(msg.lower())  # 소문자로 변환
print(msg)

tmp = msg.upper()
print(tmp)
# find() : 문자열의 제일 앞부터 인자에 해당하는 문자를 찾아서 제일 먼저 찾아진 문자의 인덱스를 반환, 없으면 -1 반환
print(tmp.find('T'))
# count() : 문자열에서 인자에 해당하는 문자의 개수를 반환
print(tmp.count('T'))
# slice: 문자열 자르기
print(msg)
print(msg[:2])
print(msg[3:5])
print(len(msg))  # 문자열의 길이
for i in range(len(msg)):
    print(msg[i], end=' ')
print()

for x in msg:
    print(x, end=' ')
print()

for x in msg:
    # if x.isupper():  # 대문자인지 확인
    if x.islower():  # 소문자인지 확인
        print(x, end=' ')
print()

for x in msg:
    if x.isalpha():  # 알파벳인지(글자인지?) 확인
        print(x, end='')
print()

tmp = 'AZ'
for x in tmp:
    print(ord(x))  # 아스키 코드값으로 변환
tmp = 'az'
for x in tmp:
    print(ord(x))  # 아스키 코드값으로 변환

tmp = 65
print(chr(tmp))  # 아스키 코드값을 문자로 변환
