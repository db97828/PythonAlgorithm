리스트 선언 총 정리 + 컴프리헨션 정리하기

리스트
: 어떠한 크기의 데이터 모음을 저장 할 수 있다.
: list 클래스로 정의된 시퀀스이다.
: 인리스트 안에 있는요소들은 인덱스를 통해 접근 할 수 있다.

리스트 생성자 사용 형식
list1 = list()                            #빈 리스트 생성
=> list = []
list2 = list([2,3,4])                     #요소 2,3,4를 가진 리스트 생성
=> list2 = [2,3,4]
list3 = list(["red","green","blue"])      #문자열들을 가진 리스트 생성
=> list3 = ["red","green","blue"]
list4 = list(range(3,6))                  #요소 3,4,5를 가진 리스트 생성
list5 = list("abcd")                      #요소 a,b,c,d를 가지는 리스트 생성
list6 = [2,"three",4]                     #파이썬은 다른 타입들끼리 리스트를 선언할 수 있다.
list7 = ['가','나','다','라',]            #리스트는 마지막 원소뒤에 콤마를 남겨도 에러가 나지 않는다. 보통 편의를 위해 마지막에 콤마를 찍기를 권장하기도 한다.
//리스트의 요소들은 콤마(,)로 분리되며 []기호로 묶는다.


시퀀스에 쓰이는 연산자
1. x in s                   : 요소 x가 시퀀스 s에 존재하면 True
2. x not in s               : 요소 x가 시퀀스 s에 존재하지 않으면 True
3. s1 + s2                  : 시퀀스 s1과 s2를 결합한다.
4. s * n, n * s             : 시퀀스 s를 n번 복사해 연결한다.
5. s[i]                     : 시퀀스 s의 i번 째 요소
6. s[i:j]                   : 시퀀스 [i]부터 [j-1]까지 자른다(slice)
7. len(s)                   : 시퀀스 s의 길이
8. min(s)                   : 시퀀스 s의 가장 작은 요소
9. max(s)                   : 시퀀스 s의 가장 큰 요소
10. sum(s)                  : 시퀀스 s의 모든 숫자들의 합
11. for loop                : for문을 이용해 리스트 왼쪽부터 오른쪽까지 요소에 접근한다.
12. <, <=, >, >=, =, !=     : 두 시퀀스를 비교한다. 


리스트 기본 사용법
1. list는 0부터 시작
a = [1,2,3]
a[0] = 1
2. 리스트에 원소 추가
list.append([원소])
3. 리스트 인덱싱/ 슬라이싱
s = 'show hot to index into sequences'.split()        #s = ['show', 'how', 'to', 'index', 'into', 'sequences']
s[0] => show
s[-1] => sequences
s[-6] => show
s[1:4] => ['how', 'to', 'index'] 
s[1:-1] => ['how', 'to', 'index', 'into']
s[3:] => ['index', 'into', 'sequences']
s[:3] => ['show', 'how', 'to']
s[3:] + s[:3] == s  => True

리스트 복사
1. full_slice = s[:]       #리스트 s를 full_slice로 복사(값은 같지만 다른 변수)
2. u = s.copy(s)
3. v = list(s)

list에 step 사용
1. s[::2]   => ['show', 'to', 'into']
2. s[::-1]  => ['sequences', 'into', 'index', 'to', 'how', 'show']

변수 간 대입
1. mutable한 객체의 변수 간 대입
a = [1,2,3]
b = a
b[0] = 5
a => [5,2,3]
b => [5,2,3]
id(a) == id(b) => True
#b에 a를 할당하면 값이 할당되는 것이 아니라 같은 메모리 주소를 바라본다. => b변경시 a도 변경됨
2. immutable한 객체
a = "abc"
b = a
id(a) == id(b) => True
b = "abcd"
a => "abc"
b => "abcd"
id(a) != id(b) => True
#list와 똑같이 b를 a에 할당하면 같은 메모리 주소를 바라본다. 
#하지만 b에 다른 값을 할당하면 재할당이 이루어지며 메모리 주소가 변경된다. => a와 b는 다른 값을 가진다

얕은 복사
#list의 슬라이싱을 통한 새로운 값을 할당 => 새로운 id가 부여되며, 서로 영향 받지 않음
a = [1,2,3]
b = a[:]
a == b => True
a is b => False
b[0] = 5
a => [1,2,3]
b => [5,2,3]

#하지만 리스트안에 리스트 mutable객ㅊ체 안에 mutable객체인 경우 
=> id(a) != id(b) 이지만, 그 내부 객체 id(a[0])과 id(b[0])은 같은 주소를 바라본다.
#재할당하는 경우는 문제 없음, 메모리 주소도 변경됨
#하지만, a[1]값을 변경하면 b[1]도 따라 변경됨

깊은복사
#내부에 객체들까지 모두 새롭게 copy되는 것
b = copy.deepcopy(a)
