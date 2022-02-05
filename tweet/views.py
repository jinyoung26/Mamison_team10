from django.shortcuts import render, redirect
from .models import  tweetmodel, tweetcommant
from django.http import JsonResponse
from django.views import View
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

    return render(request,'main.html', {"tweet": all_tweet})


# @login_required
# def detail_tweet(request, id):
#     my_tweet = TweetModel.objects.get(id=id)
#     all_comment = TweetComment.objects.filter(tweet_id=id).order_by('-created_at')
#     if request.method == "GET":
#         return render(request, "tweet/tweet_detail.html", {"tweet": my_tweet, 'comment': all_comment})
#
#
#
# def qmain(self,request,id):
#     all_tag=tweetmodel.objects.get(tag= id)
#
#     return render(request,'main.html',{"tweet":all_tag})


class taglistview(View):
    def get(self, request):
        try:
            name = request.GET.get('name')
            products = tweetmodel.objects.filter(tag=name).values()
            products = list(products)

            return JsonResponse({'message': 'SUCCESS', 'products': products}, status=200)
        except ValueError:
            return JsonResponse({'message': 'VALUE_ERROR'}, status=400)





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

        return render(request, 'detail.html',{"tweet": my_tweet,"tag":taglist,"comment": all_comment})
    # , '

# @login_required  # 로그인이 되어있어야 실행가능
def write_comment(request, id):
    if request.method == "POST":
        T_comment = tweetcommant()

        T_comment.comment = request.POST.get("comment", '')  ##post로 name이 comment인 html의 요소안에서 텍스트를 가져온다
        T_comment.tweet = tweetmodel.objects.get(id=id)  ## 댓글창 열기전 트위터 개시물 아이디
        T_comment.author = request.user  ## 로그인한 유저
        T_comment.save()
        return redirect(f"/detail/{id}")  # 선택한 트위터의 댓글달기 창으로 다시 돌려줌

# @login_required  # 로그인이 되어있어야 실행가능
def delete_comment(request, id):
    tweet_comment = tweetcommant.objects.get(id=id)
    current_tweet = tweet_comment.tweet.id  ## 지우기전에 트위터에 해당하는 id를 빼온다
    tweet_comment.delete()
    return redirect(f'/detail/{current_tweet}')

