"""
작성일: 2020-08-26
==============================================================================
문제: 재귀 함수로 구현한 이진 탐색 소스코드
==============================================================================
소요 시간: 00분
"""

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid + 1, end)

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)

"""
접근법: 내가 왜 이런 방식으로 문제를 해결했는지 작성
==============================================================================
다른 해결 방식: 다른 해결 방법
==============================================================================
개선점: 개선할 수 있는 부분
==============================================================================
노트: 기타 내용
"""