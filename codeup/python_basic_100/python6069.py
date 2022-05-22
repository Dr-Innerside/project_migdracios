# 6069

# 평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.

# 평가 내용
# 평가 : 내용
# A : best!!!
# B : good!!
# C : run!
# D : slowly~
# 나머지 문자들 : what?

status = input()


def is_what(status):
    if status == 'A':
        comment = 'best!!!'
    elif status == 'B':
        comment = 'good!!'
    elif status == 'C':
        comment = 'run!'
    elif status == 'D':
        comment = 'slowly~'
    else:
        comment = 'what?'
    return comment


result = is_what(status)

print(result)
