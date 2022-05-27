# 6070

# 월이 입력될 때 계절 이름이 출력되도록 해보자.

# 월 : 계절 이름
# 12, 1, 2 : winter
#   3, 4, 5 : spring
#   6, 7, 8 : summer
#   9, 10, 11 : fall

month = int(input())


def is_season(month):
    season = {
        'winter': [12, 1, 2],
        'spring': [3, 4, 5],
        'summer': [6, 7, 8],
        'fall': [9, 10, 11]
    }
    if month in season['winter']:
        target_season = 'winter'
    elif month in season['spring']:
        target_season = 'spring'
    elif month in season['summer']:
        target_season = 'summer'
    else:
        target_season = 'fall'
    return target_season


result = is_season(month)
print(result)
