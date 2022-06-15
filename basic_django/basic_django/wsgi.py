# """
# WSGI config for basic_django project.

# It exposes the WSGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
# """

# import os
# from turtle import title

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'basic_django.settings')

# application = get_wsgi_application()


# #divConfirmedMaterialArea > ul > a:nth-child(2) > li

# {title : '보끔밥'}
# {image_url : 'djfklajslkf;.jpg'}
# {difficulty : '아무나'}
# {timecost : 15}
# {ing : ['밥', '식용유', '양파']}
# {detail : '1.밥을 짓습니다 \n 2.밥을 볶습니다 \n 3.먹습니다'}

# recipe = [title, image_url, difficulty, timecost, ing, detail]

# pandas를 이용해서 csv 데이터를 만들기(각각 요소는 필드로 들어간다!)


# list = ['hys', 'kti', 'khj']
# print(id(list))
# print(id(list[0]))
# print(id(list[1]))
# print(id(list[2]))

# list[0] = 'lmk'
# print(id(list))

tuple_ = ('hys', 'kti')
print(id(tuple_))
tuple_[0] = 'khj'
