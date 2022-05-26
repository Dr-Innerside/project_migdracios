# my_age = 100

# if my_age == 100:
#     print("저는 100살입니다")
# else:
#     print("거짓말")

# jumsu_list = [90,20, 100 ,80 ,70]
# for jumsu in jumsu_list:
#     print(jumsu)

class POST:
    id = ''
    title = ''
    author = ''
    content = ''

first_post = POST()
POST.id = 'ys20473'
POST.title = '오늘의 일기'
POST.author = '황영상'
POST.content = '오늘 먹은 것은 탕수육'

print(POST.id)
print(POST.title)
print(POST.author)
print(POST.content)