# 6068

# 점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.

# 평가 기준
# 점수 범위 : 평가
#  90 ~ 100 : A
#  70 ~   89 : B
#  40 ~   69 : C
#    0 ~   39 : D
# 로 평가되어야 한다.


score = int(input())


def grade(score):
    if score >= 90:
        # print('A')
        grade = 'A'
    elif score >= 70:
        # print('B')
        grade = 'B'
    elif score >= 40:
        # print('C')
        grade = 'C'
    else:
        # print('D')
        grade = 'D'
    return grade


result = grade(score)
print(result)
