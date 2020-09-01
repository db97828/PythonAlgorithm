"""
작성일: 2020-08-26
==============================================================================
문제: 부품 찾기
부품이 N개 있고, 각 부품은 정수 형태의 고유한 번호가 있다.
손님이 M개 종류의 부품을 대량으로 구매하겠다며 견적서를 요청했다.
이때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성해보자
==============================================================================
소요 시간: 00분
"""

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            start = mid + 1
        else:
            end = mid - 1
    return None

n = int(input())
shop_array = list(map(int, input().split()))
m = int(input())
customer_array = list(map(int, input().split()))

for i in customer_array:
    result = binary_search(shop_array, i, 0, n - 1)
    if result != None:
        print("yes", end=' ')
    else:
        print("no", end=' ')
"""
접근법: 손님이 확인 요청한 전체 부품 번호를 이진탐색으로 하나씩 확인함
==============================================================================
다른 해결 방식: 계수 정렬

n = int(input())
array = [0] * 1000000                       # 범위 만큼 길이의 array를 생성      

for i in input().splite():                  # 가게에 있는 전체 부품 번호를 입력받아서 기록
    array[int(i)] = 1                       # 입력받은 숫자의 위치를 1로 변경
    
m = int(input())
x = list(map(int, input().split())

for i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')
        
다른 해결 방식 : set()함수 => 단순히 특정한 데이터가 존재하는지 검사할 때 매우 효과적으로 사용할 수 있다.

n = int(input())
array = set(map(int, input().split()))              #가게에 있는 전체 부품 번호를 받아서 집합 자료형에 기록
m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end= ' ')
    else:
        print('no', end=' ')

==============================================================================
개선점: 개선할 수 있는 부분
==============================================================================
노트: set()함수 더 공부하기
"""