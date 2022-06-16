users = ['황영상', '이민기', '김태인', '김희정']
user_email = {'황영상':'ys20473', '이민기':'psjlmk', '김태인':'kti091', '김희정':'kimheejeong'}
def show_user(*args, **kwargs):
    for user in args:
        print(user, end=' ')
    for email in kwargs.items():
        print(email[1], end=' ')

show_user(*users, **user_email)

