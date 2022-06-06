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
        all_tweet = TweetModel.objects.all().order_by('-create_at')
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

def view_tweet(request, id):
    target_tweet = TweetModel.objects.get(id=id)
    return render(request, 'tweet/tweet_detail.html', {'tweet': target_tweet})

def comment(request):
    comment = request.POST.get('comment')

    return ''

def delete_comment(request):
    return ''