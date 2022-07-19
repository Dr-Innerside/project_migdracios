input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    # 이 부분을 채워보세요!
    
    # 배열 내에서 가장 큰 수를 찾아내기
    # 반복문으로 슬라이싱
    # 큰수를 반복하고 가장 큰 수를 변수로 초기화
    max_num = 1
    for i in input:
        if i > max_num:
            print(i)
            max_num = i
            print(max_num)
    return max_num


result = find_max_num(input)
print(result)