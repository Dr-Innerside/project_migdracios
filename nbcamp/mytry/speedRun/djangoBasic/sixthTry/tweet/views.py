from django.shortcuts import render, redirect
from .models import TweetModel
# Create your views here.
def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/tweet')
    else:
        return redirect('/sign-in')

def tweet(request):
    if request.method == 'GET':
        all_tweet = TweetModel.objects.all()
        user = request.user.is_authenticated
        if user:
            return render(request, 'tweet/home.html', {'tweet': all_tweet})

    elif request.method == 'POST':
        author = request.user
        content = request.POST.get('my-content')

        new_tweet = TweetModel()
        new_tweet.author = author
        new_tweet.content = content
        new_tweet.save()
        return redirect('/tweet')