"""
작성일: 2020-09-08
==============================================================================
문제: 문자열 압축
==============================================================================
소요 시간: 00분
"""


def solution(s):
    string_length = len(s)
    split_length = len(s) // 2

    for i in range(1, split_length + 1):
        temp = []
        temp_string = ""
        for j in range(0, len(s), i):
            temp.append(s[j:j + i])
        compare_word = temp[0]
        word_length = 1
        for word in temp[1:]:
            if compare_word == word:
                word_length += 1
            else:
                if word_length == 1:
                    temp_string += compare_word
                else:
                    temp_string += str(word_length) + compare_word
                compare_word = word
                word_length = 1
        if word_length == 1:
            temp_string += word
        else:
            temp_string += str(word_length) + compare_word
        if len(temp_string) < string_length:
            string_length = len(temp_string)

    print(string_length)


s = input()
solution(s)
"""
접근법: 내가 왜 이런 방식으로 문제를 해결했는지 작성
==============================================================================
다른 해결 방식: 다른 해결 방법
def solution(s):
    string_length = len(s)
    split_length = len(s) // 2
    
    for i in range(1, split_length + 1):
        temp = []
        temp_string = ""
        for j in range(0, string_length, i):
            temp.append(s[j:j+i])
        compare_word = temp[0]
        word_length = 1
        for word in temp[1:]:
            if compare_word == word:
                word_length += 1
            else:
                if word_length == 1:
                    temp_string += compare_word
                else:
                    temp_string += str(word_length) + compare_word
                word_length = 1
                compare_word = word
        if word_length == 1:
            temp_string += word
        else:
            temp_string += str(word_length) + compare_word
    if string_length > len(temp_string):
        string_length = len(temp_sting)

    print(string_length)

s = input()
solution(s)
==============================================================================
개선점: 개선할 수 있는 부분
==============================================================================
노트: 기타 내용
"""
