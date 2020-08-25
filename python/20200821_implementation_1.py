"""
작성일: 2020-08-21
==============================================================================
문제: 왕실의 나이트
나이트는 말을 타고 있기 때문에 이동을 할 때는 L자 형태로만 이동할 수 있으며 정원 밖으로는 나갈 수 없다.
1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기
좌표 평면상에서 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램 작성
행 위치는 1부터 8로 표현하며, 열 위치는 a부터 h로 표현한다.
==============================================================================
소요 시간: 00분
"""
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [
    (-2, -1), (-1, -2), (1, -2), (2, -1),
    (2, 1), (1, 2), (-1, 2), (-2, 1)
]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if 1 <= next_row <= 8 and 1 <= next_column <= 8:
        result += 1

print(result)

"""
접근법: steps에 가능한 경우를 저장해 놓고 범위안에 있는지 확인하여 가능하면 result++을 해줌
==============================================================================
다른 해결 방식: 다른 해결 방법
"""
"""
position = input()
row = int(position[1])
column = int(ord(position[0])) - int(ord('a')) + 1

result = 0

steps = [
    (-2, -1), (-1, -2), (1, -2), (2 , -1),
    (2, 1), (1, 2), (-1, 2), (-2, 1)
]

for step in steps:
    row_next = row + step[0]
    column_next = column + step[1]
    if 1 <= row_next <= 8 and 1 <= column_next <= 8:
        result += 1
        
print(result)
"""
"""
==============================================================================
개선점: 개선할 수 있는 부분
==============================================================================
노트:
파이썬에서는 문자열을 배열로 받기때문에 바로 배열로 사용 가능
'1 <= next_row <= 8' 이런 형태 가능
 ord('a')는 a의 숫자값 반환해줌 
"""