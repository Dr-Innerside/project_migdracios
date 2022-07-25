'''
사칙연산
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	301158	144778	125509	48.590%
문제
두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 

입력
두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)

출력
첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.
'''

A,B = map(int, input().split())
def calc(num1, num2):
    print(num1+ num2)
    print(num1- num2)
    print(num1* num2)
    print(num1// num2) # / 한 개는 실수 나눗셈, // 두 개는 정수 나눗셈이다
    print(num1% num2)
calc(A,B)
    