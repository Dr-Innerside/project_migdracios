# 6065

# 3개의 정수(a, b, c)가 입력되었을 때, 짝수만 출력해보자.


a, b, c = map(int, input().split())


def is_jjak(num):
    if num % 2 == 0:
        print(num)


is_jjak(a)
is_jjak(b)
is_jjak(c)
