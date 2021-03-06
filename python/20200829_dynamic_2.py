"""
작성일: 2020-08-29
==============================================================================
문제: 개미전사
식량창고가 일직선상일 때 최소한 한 칸 이상 떨어진 식량창고를 약탈해야 한다.
식량창고 N개에 대한 정보가 주어졌을 때 얻을 수 있는 식량의 최대값을 구하는 프로그램을 작성하시오
==============================================================================
소요 시간: 00분
"""

n = int(input())
k = list(map(int, input().split()))

d = [0] * 100

d[0] = k[0]
d[1] = max(k[0], k[1])
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + k[i])

print(d[n - 1])

"""
접근법: i-1과 i-2+k[i] 중 큰 수를 찾기  
==============================================================================
다른 해결 방식: 다른 해결 방법
==============================================================================
개선점: 창고가 1개일때부터 하나하나 생각해보기! 
==============================================================================
노트: i-3번째 이하의 식량창고는 왜 고려할 필요가 없는지 이해가 잘 안됨ㅜㅜ
"""