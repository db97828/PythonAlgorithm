"""
작성일: 2020-08-20
==============================================================================
문제: 1이 될 때까지
다음 두 과정 중 하나를 반복적으로 선택하여 수행하여 1이 될 때까지 수행해야 하는 최소 횟수를 구하여라
단, 두 번째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다.
1. N에서 1을 뺀다
2. N을 K로 나눈다.
==============================================================================
소요 시간: 00분
"""

n, k = map(int, input().split())

count = 0

while n >= k:
    if n % k != 0:
        n -= 1
        count += 1
    else:
        n //= k
        count += 1

while n > 1:
    n -= 1
    count += 1
    
print(count)

"""
접근법: k로 나눠서 딱 떨어지지 않으면 1을 빼고, 아니면 나누어 주면서 1을 만들었다
==============================================================================
다른 해결 방식: 다른 해결 방법

n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target
    if n < k:
        break
    result += 1
    n //= k

result += (n - 1)
print(result)

==============================================================================
개선점: 1을 한번에 빼고, 마지막에 1을 빼는 것도 두가지 경우를 수식으로 한번에 표시하기
==============================================================================
노트: 기타 내용
"""