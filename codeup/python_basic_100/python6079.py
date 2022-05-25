# 6079

# 1, 2, 3 ... 을 계속 더해 나갈 때,
# 그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지만
# 계속 더하는 프로그램을 작성해보자.

# 즉, 1부터 n까지 정수를 계속 더해 나간다고 할 때,
# 어디까지 더해야 입력한 수보다 같거나 커지는 지를 알아보고자하는 문제이다.

# -- logic --
# 1. 입력
# 2. 입력한 수까지 1부터 더해나가기
# 3. 이게 1000보다 크면 멈추고 마지막에 더한 수를 프린트


mynum = int(input())
sum = 0
startNum = 1



while mynum != startNum:

    sum += startNum
    # print(f'반복 시도 : mynum: {mynum}, startNum: {startNum} sum: {sum}')
    startNum += 1

    if mynum == startNum:
        # print(f'입력 값까지 더했다! {mynum}=={startNum}')
        break

    # print(f'sum 값 체크 {sum}')

    if sum >= 1000:
        # print(f'sum 1000초과! 마지막으로 더한 정수는~ {startNum}')
        print(startNum)
        break

    
