# 6078

# 영문 소문자 'q'가 입력될 때까지
# 입력한 문자를 계속 출력하는 프로그램을 작성해보자.


mychar = input()

if mychar == 'q':
        print(mychar)
        
while mychar != 'q' :
    print(mychar)
    mychar = input()

    if mychar == 'q':
        print(mychar)
        break



# ---- LOGIC ----
# 1. 문자 하나를 입력받음
# 2. 입력한 문자가 소문자 q가 아니라면 q가 나올때까지 입력한 문자를 출력하기