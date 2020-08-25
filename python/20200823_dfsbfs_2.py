"""
작성일: 2020-08-23
==============================================================================
문제: 미로 탈출
N X M 크기의 직사각형 형태의 미로에 갇혀 있다.
현재 위치는 (1,1)이고, 출구는 (N,M)이다
한 번에 한 칸씩 이동할 수 있다.
괴물이 있는 부분은 0, 없는 부분은 1로 표시되어 있다.
탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오.
시작 칸과 마지막 칸을 모두 포함해서 계산한다.
==============================================================================
소요 시간: 00분
"""
from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n - 1][m - 1]


print(bfs(0, 0))

"""
접근법: 내가 왜 이런 방식으로 문제를 해결했는지 작성
==============================================================================
다른 해결 방식: 다른 해결 방법
==============================================================================
개선점: 개선할 수 있는 부분
==============================================================================
노트: 기타 내용
"""
