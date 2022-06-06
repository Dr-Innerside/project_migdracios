from django.shortcuts import render, redirect
from .models import TweetModel, TweetComment
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
    target_comment = TweetComment.objects.filter(tweet=id).order_by('-created_at')
    return render(request, 'tweet/tweet_detail.html', {'tweet': target_tweet, 'comment':target_comment})

def comment(request, id):
    tweet = TweetModel.objects.get(id=id)
    author = tweet.author
    comment = request.POST.get('comment')
    new_comment = TweetComment()
    new_comment.tweet = tweet
    new_comment.author = author
    new_comment.comment = comment
    new_comment.save()

    return redirect(f'/tweet/{id}')

def delete_comment(request):
    return ''