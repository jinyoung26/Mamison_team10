from django.shortcuts import render
from django.contrib.auth.decorators import login_required  ## 함수위에 붙어있음 로근인이 되어있어야 실행가능

#### 크롤링
import requests
import pandas as pd
from newspaper import Article
from bs4 import BeautifulSoup
###크롤링


# Create your views here.
def main(request):
    # temp_url = 'https://terms.naver.com/search.naver?query=123&searchType=text&dicType=&subject='
    # temp_url1 = temp_url.split('123')[0]
    # temp_url2 = temp_url.split('123')[1]
    # url = (f'{temp_url1}{data}{temp_url2}')
    # print(url)
    # data = requests.get(url, headers=headers)
    # soup = BeautifulSoup(data.text, 'html.parser')
    # info = soup.select_one('#content > div:nth-child(3) > ul > li:nth-child(1) > div.info_area > p').text
    # return info

    return render(request, 'main.html')


# @login_required
# def detail_tweet(request, id):
#     my_tweet = TweetModel.objects.get(id=id)
#     all_comment = TweetComment.objects.filter(tweet_id=id).order_by('-created_at')
#     if request.method == "GET":
#         return render(request, "tweet/tweet_detail.html", {"tweet": my_tweet, 'comment': all_comment})
#
#
