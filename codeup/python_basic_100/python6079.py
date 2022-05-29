# 6079

# 1, 2, 3 ... 을 계속 더해 나갈 때,
# 그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지만
# 계속 더하는 프로그램을 작성해보자.

# 즉, 1부터 n까지 정수를 계속 더해 나간다고 할 때,
# 어디까지 더해야 입력한 수보다 같거나 커지는 지를 알아보고자하는 문제이다.

# -- logic --
# 1. 입력
# 2. 입력한 수까지 1부터 더해나가기
# 3. 합이 입력한 수와 같아질 때 멈추기

# while mynum != startNum:
#
#     sum += startNum
#     # print(f'반복 시도 : mynum: {mynum}, startNum: {startNum} sum: {sum}')
#     startNum += 1
#
#     if mynum == startNum:
#         # print(f'입력 값까지 더했다! {mynum}=={startNum}')
#         break
#
#     # print(f'sum 값 체크 {sum}')
#
#     if sum >= 1000:
#         # print(f'sum 1000초과! 마지막으로 더한 정수는~ {startNum}')
#         print(startNum)
#         break
#
#



# while mynum >= startNum:
#     # print(f'진입합니다 {startNum}')
#
#     sum += startNum
#     startNum += 1
#
# print(sum)
#

# print('숫자를 하나 입력해주세요')
# mynum = int(input())
# sum = 0
# startNum = 1
#
# def lastNum(mynum, sum=0, startNum=1):
#     while mynum != sum :
#         # print(f'{startNum} 번째 진입')
#         sum += startNum
#         # print(f'지금까지 합한 수 {sum}')
#         if mynum == sum:
#             break
#         startNum += 1
#         # print(f'start num ->{startNum}')
#     print(startNum)
#
# lastNum((mynum))
def last_num(mynum, startNum=1, sum=0):
    for sequence in range(mynum):
        if mynum <= sum:
            return startNum-1
        else:
            sum+=startNum
            startNum+=1
            # print(f'sum->{sum}')
mynum = int(input())
result = last_num(mynum)
print(result)