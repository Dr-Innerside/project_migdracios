# 1. args, kwargs를 사용하는 예제 코드 짜보기

list_ = [1,2,3,4,5]
print(f"list_->{list_}")
print(*list_)

def sum_input(*args):
    return sum(args)

sum_result = sum_input(*list_)
print(f"input args and result is ->{sum_result}")

dict_ = {
    "name": "yungsang",
    "age": 29,
    "stuborn": True
}
print(f"dict_->{dict_}")
# print(**dict_)

def who(**kwargs):
    name = kwargs["name"]
    age = kwargs["age"]
    stuborn = kwargs["stuborn"]
    print(f"This is {name}, age is {age}, stuborn is {stuborn}")

who(**dict_)