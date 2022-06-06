from django.shortcuts import render, redirect
from .models import TweetModel
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/tweet')
    else:
        return redirect('/sign-in')

def tweet(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        all_tweet = TweetModel.objects.all().order_by('-created_at')
        if user:
            return render(request, 'tweet/home.html', {'tweet': all_tweet})
        else:
            return redirect('/sign-in')
    if request.method == 'POST':
        user = request.user
        content = request.POST.get('my-content')
        new_tweet = TweetModel()
        new_tweet.author = user
        new_tweet.content = content
        new_tweet.save()
        return redirect('/tweet')

def delete_tweet(request, id):
    my_tweet = TweetModel.objects.get(id=id)
    my_tweet.delete()
    return redirect('/tweet')