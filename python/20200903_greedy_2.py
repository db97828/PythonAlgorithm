"""
작성일: 2020-09-03
==============================================================================
문제: 곱하기 혹은 더하기
각 자리가 숫자(0~9)로만 이루어진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며
수자 사이에 'x'혹은 '+'연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오.
==============================================================================
소요 시간: 00분
"""

s = input()

result = int(s[0])

for i in range(1, len(s)):
    num = int(s[i])
    if result <= 1 or num <= 1:
        result += num
    else:
        result *= num

print(result)

"""
접근법: 연산할 두 수 중에서  0 or 1 이면 더하기 아니면 곱하기 넣기
==============================================================================
다른 해결 방식: 다른 해결 방법
==============================================================================
개선점: 개선할 수 있는 부분
==============================================================================
노트: 기타 내용
"""