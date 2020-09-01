"""
작성일: 2020-08-29
==============================================================================
문제: 바닥공사
가로의 길이가 N, 세로의 길이가 2인 직사각형 형태의 얇은 바닥이 있다.
1 X 2, 2 X 1, 2 X 2의 덮개를 이용해 채울 때,
바닥을 채우는 모든 경우의 수를 구하여라
==============================================================================
소요 시간: 00분
"""

n = int(input())

d = [0] * 1001

"""
접근법:   
==============================================================================
다른 해결 방식: 다른 해결 방법
==============================================================================
개선점: 개선할 수 있는 부분
==============================================================================
노트: 
결과를 어떤 수로 나눈 결과를 출력하라 => 결과값이 굉장히 커질 수 있기 때문 
=> 값을 계산할 때마다 특정한 수로 나눈 나머지만 취하도록 하면 된다.
"""