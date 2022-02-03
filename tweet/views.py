from django.shortcuts import render
from .models import tweetmodel,tweetcommant
from django.contrib.auth.decorators import login_required  ## 함수위에 붙어있음 로근인이 되어있어야 실행가능

# #### 크롤링
# import requests
# import pandas as pd
# from newspaper import Article
# from bs4 import BeautifulSoup
# ###크롤링


# Create your views here.
def main(request):
    all_tweet = tweetmodel.objects.all()

    return render(request, 'main.html', {"tweet": all_tweet})


# @login_required
# def detail_tweet(request, id):
#     my_tweet = TweetModel.objects.get(id=id)
#     all_comment = TweetComment.objects.filter(tweet_id=id).order_by('-created_at')
#     if request.method == "GET":
#         return render(request, "tweet/tweet_detail.html", {"tweet": my_tweet, 'comment': all_comment})
#
#

def qmain(request,id):
    all_tag=tweetmodel.objects.get(tag= id)
    return render(request,'main.html',{"tweet":all_tag})




def detail_view(request, id):
    my_tweet = tweetmodel.objects.get(id=id)
    all_comment = tweetcommant.objects.filter(tweet_id=id)
    if request.method == "GET":
        taglist =""
        tags=my_tweet.tag
        list(tags)
        for i in range(0, 4):
            tag = tags.split(",")[i]
            print(tag)
            if tag != "전체":
                taglist = taglist + " " + tag
                print("-----")
                print(taglist)








        return render(request, 'detail.html',{"tweet": my_tweet,"tag":taglist})
    # , 'comment': all_comment

