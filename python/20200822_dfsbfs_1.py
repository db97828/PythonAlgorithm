"""
작성일: 2020-08-22
==============================================================================
문제: 음료수 얼려먹기
n X m 크기의 얼음 틀이 있다.
구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
구멍이 뚫려 있는 부분끼리 상하좌우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수 구하여라

==============================================================================
소요 시간: 00분
"""

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
"""
접근법: 내가 왜 이런 방식으로 문제를 해결했는지 작성
==============================================================================
다른 해결 방식: 다른 해결 방법
==============================================================================
개선점: 개선할 수 있는 부분
==============================================================================
노트:
dfs(i, j) == True   => dfs(i, j)로 쓸 수 있다
"""