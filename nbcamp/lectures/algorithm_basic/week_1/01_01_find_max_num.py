input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    # 이 부분을 채워보세요!
    
    """
    나의 풀이
    
    배열 내에서 가장 큰 수를 찾아내기
    반복문으로 슬라이싱
    큰수를 반복하고 가장 큰 수를 변수로 초기화
    
     max_num = 0
    for i in array:
        #3 5 6 1 2 4
        if i > max_num:
            max_num = i
    return max_num
    """
    
   
    
    # 숫자를 비교하는 방식
    for num in array:
        #3 5 6 1 2 4
        for compare_num in array:
            #3 5 6 1 2 4
            if num < compare_num:
                break
        else:
            return num


result = find_max_num(input)
print(result)