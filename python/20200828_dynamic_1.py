"""
작성일: 2020-08-28
==============================================================================
문제: 1로 만들기
정수 x가 주어질 때 정수 x에 사용할 수 있는 연산은 다음과 같다.
1. x가 5로 나누어떨어지면, 5로 나눈다.
2. x가 3으로 나누어떨어지면, 3으로 나눈다.
3. x가 2로 나누어떨어지면, 2로 나눈다.
4. x에서 1을 뺀다.
연산을 사용하여 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오
==============================================================================
소요 시간: 00분
"""
x = int(input())

d = [0] * 30001

for i in range(2, x + 1):
    d[i] = d[i - 1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])

"""
접근법: d[2]부터 저장해 놓고 사용하기
==============================================================================
다른 해결 방식: 다른 해결 방법
    
==============================================================================
개선점: 개선할 수 있는 부분
==============================================================================
노트: 어려움, 다시 풀어보기
"""