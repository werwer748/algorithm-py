"""
최솟값 구하기
"""

arr = [5, 3, 7, 9, 2, 5, 2, 6]
# float('inf'): 파이썬에서 가장 큰값 무한대
arrMin = float('inf')
for i in range(len(arr)):
    if arr[i] < arrMin:  # 가장 큰 숫자부터 배열 내부의 숫자들순으로 돌면서 점점 작은수를 집어 넣는다.
        arrMin = arr[i]

"""
arrMin = arr[0]
for i in range(1, len(arr)):
    if arr[i] < arrMin:
        arrMin = arr[i]
        
arrMin = float('inf')
for x in arr:
    if x < arrMin:
        arrMin = x
"""

print(arrMin)

