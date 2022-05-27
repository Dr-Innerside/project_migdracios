# 6066

# 3개의 정수(a, b, c)가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.

a, b, c = map(int, input().split())


def is_what(num):
    if num % 2 == 0:
        print('even')
    else:
        print('odd')


is_what(a)
is_what(b)
is_what(c)
