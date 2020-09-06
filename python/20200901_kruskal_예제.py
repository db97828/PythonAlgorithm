"""
작성일: 2020-09-01
==============================================================================
문제: 크루스칼 알고리즘 소스코드
==============================================================================
소요 시간: 00분
"""

#특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

#두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

#노드의 개수와 간선의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1)              #부모 테이블 초기화

edges = []
result = 0

#부모 테이블상에서 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

#모든 간선에 대한 저보를 입력받기
for _ in range(e):
    a, b, cost = map((int, input().split()))
    #비용순으로 정렬하기 위해 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)


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