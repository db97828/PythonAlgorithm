"""
작성일: 2020-09-08
==============================================================================
문제: 괄호 변환
==============================================================================
소요 시간: 00분
"""

def divide(w):
    opne = 0
    close = 0
    for i in w:
        if i == '(':
            opne += 1
        else:
            close += 1
        if open == close:
            return w[:i + 1], w[i + 1:]


def isBalenced(u):
    temp = []

    for p in u:
        if p == '(':
            temp.append(p)
        else:
            if not temp:
                return False
            temp.pop()
    return True


def solution(w):
    if not w:
        return ""

    u, v = divide(w)

    if isBalenced(u):
        return u + solution(v)
    else:
        temp_str = '('
        temp_str += solution(v)
        temp_str += ')'

        for j in u[1:len(u) - 1]:
            if j == '(':
                temp_str += ')'
            else:
                temp_str += '('

        return temp_str

"""
접근법: 내가 왜 이런 방식으로 문제를 해결했는지 작성
==============================================================================
다른 해결 방식: 다른 해결 방법
==============================================================================
개선점: 개선할 수 있는 부분
==============================================================================
노트: 기타 내용
"""
