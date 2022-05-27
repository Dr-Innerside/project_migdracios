# 6073

# 정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.

num = int(input())

while num >= 0:
    num -= 1
    if num < 0:
        break
    else:
        print(num)
