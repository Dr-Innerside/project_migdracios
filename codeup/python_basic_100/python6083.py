# 6083
#
# 빨강(red), 초록(green), 파랑(blue) 빛을 섞어 여러 가지 다른 색 빛을 만들어 내려고 한다.
#
# 빨강(r), 초록(g), 파랑(b) 각 빛의 가짓수가 주어질 때,
# 주어진 rgb 빛들을 섞어 만들 수 있는 모든 경우의 조합(r g b)과 만들 수 있는 색의 가짓 수를 계산해보자.

# c1, c2, c3 = map(int, input().split())
# color =[]
# # color = [r for r in range(c1) for g in range(c2) for b in range(c3) ]
# # print(color)
# for r in range(c1):
#     for g in range(c2):
#         for b in range(c3):
#             print(r, g, b)
#             color.append([r,g,b])
# print(len(color))

# c1, c2, c3 = map(int, input().split())
# colors = [(r,g,b) for r in range(c1) for g in range(c2) for b in range(c3)]
# for c in colors:
#     print(c)
# print(len(colors))

# --- 색의 경우의 수 --- #
# 1. 정수 세 개를 입력 받는다

c1, c2, c3 = map(int, input().split())

# 2. 경우의 수 0 1 2 를 출력해보자

# for i in range(0, c1+1):
    # print(i)

# 2. 중첩해서 0 0 을 출력해보자

# for i in range(0, c1+1):
#     for j in range(0, c2+1):
#         print(i, j)

# 3. 세 개 다 출력
# for i in range(0, c1+1):
#     for j in range(0, c2+1):
#         for k in range(0, c3+1):
#             print(i, j, k)

#4. 0에서 1까지만
#5. 출력한 경우의 수를 보여주기
sum = 0
for i in range(c1):
    for j in range(c2):
        for k in range(c3):
            print(i, j, k)
            sum += 1
print(sum)

