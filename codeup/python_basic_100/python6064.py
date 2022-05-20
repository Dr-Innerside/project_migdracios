# 6064

# 입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자.
# 단, 3항 연산을 사용한다.

a, b, c = map(int, input().split())
#   --- 세 값 중 가장 큰 값을 뽑기 위해서는
#   --- 조건문으로 일일이 비교해야 할까?
#   --- 좀 더 객체지향적으로!

#   --- 조건문
#   --- a, b, c 를 비교해야됨
#   --- a b
#   --- b c
#   --- c a
def big_number(num1, num2, num3):

    biggest = num1 if num1>num2 else num2
    
    if biggest == num1:
        biggest = num1 if num1>num3 else num3
        return biggest
    elif biggest == num2:
        biggest = num2 if num2>num3 else num3
        return biggest
    
result = f'답은 {big_number(a,b,c)}'
print(result)