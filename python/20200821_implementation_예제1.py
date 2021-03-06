"""
작성일: 2020-08-21
==============================================================================
문제: 상하좌우
계획서가 주어졌을 때 여행가 A가 최종적으로 도착할 지점의 좌표를 출력하는 프로그램 작성하시오
L:왼쪽으로 한 칸 이동
R:오른쪽으로 한 칸 이동
U:위로 한 칸 이동
D:아래로 한 칸 이동
A가 N X N 크기의 정사각형 공간을 벗어나는 움직임은 무시된다.
==============================================================================
소요 시간: 00분
"""
n = int(input())
plans = input().split()
x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

#이동 계획 하나씩 확인
for plan in plans:
    print(plan)
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    #공간을 벗어나면 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)

"""
접근법: 내가 왜 이런 방식으로 문제를 해결했는지 작성
==============================================================================
다른 해결 방식: 다른 해결 방법
==============================================================================
개선점: 개선할 수 있는 부분
==============================================================================
노트:
for plan in plans #plans에 있는 배열을 앞에서 부터 순서대로 하나씩...
"""