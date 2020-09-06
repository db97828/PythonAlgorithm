"""
작성일: 2020-09-01
==============================================================================
문제: 서로소 집합을 활용한 사이클 판별 소스코드
==============================================================================
소요 시간: 00분
"""


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0] * (v + 1)

for i in range(1, v + 1):
    parent[i] = i

cycle = False

for i in range(e):
    a, b = map((int, input().split()))
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

if cycle:
    print('사이클이 발생했습니다.')
else:
    print('사이클이 발생하지 않았습니다.')


"""
접근법: 내가 왜 이런 방식으로 문제를 해결했는지 작성
==============================================================================
다른 해결 방식: 다른 해결 방법
==============================================================================
개선점: 개선할 수 있는 부분
==============================================================================
노트: 
플루이드도 경우의수가 정해진 경우 다익스트라 가능하다xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
반복변수 잘 설정하기(알아보기 쉽도록)
"""