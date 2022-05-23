# 6075

# 정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.

mynum = int(input())
startNum = 0

while mynum >= startNum:
    print(startNum, end=" ")
    startNum += 1
