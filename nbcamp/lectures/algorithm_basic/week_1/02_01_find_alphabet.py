# hwang yung sang 이라는 문자의 최빈값 구하기
# ord, 배열 사용하기

target_char = "coding of co"

# 먼저 알파벳인지 검사
target_char = list(target_char)
list_char = []
for char in target_char:
    if str.isalpha(char):
        list_char.append(char)
print(list_char)

# 알파벳 빈도 수 찾기
alphabet_list = [0]*26

# 잘라진 글자의 ord 값을 구해서 배열 인덱스에 넣기
for char in list_char:
    # ord a의 값을 뺀 인덱스의 넘버를 구하고, 거기 번호에 +1하기
    index_num = ord(char) - ord('a')
    alphabet_list[index_num] += 1

print(alphabet_list)
# 알파벳 리스트에서 최빈값 찾기 --> max_num
max_num = alphabet_list[0]
for num in alphabet_list:
    if num > max_num:
        max_num = num
target_alpha = chr(ord('a')+max_num)

