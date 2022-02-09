from django.shortcuts import render, redirect
from .models import  tweetmodel, tweetcommant
from django.http import JsonResponse
from django.views import View
import tensorflow as tf
import h5py
import csv
import pandas as pd
from konlpy.tag import Mecab
from numpy.ma.extras import average
from gensim.test.utils import common_texts
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from django.contrib.auth.decorators import login_required  ## 함수위에 붙어있음 로근인이 되어있어야 실행가능
# #### 크롤링
# import requests
# import pandas as pd
# from newspaper import Article
# from bs4 import BeautifulSoup
# ###크롤링
# Create your views here.
# def make_token(csv):
#     # 형태소 분석을 위한 객체를 만들고,
#     mecab = Mecab()
#     # 형태소 분석된 결과를 저장하기 위한 token 열을 생성해서 0으로 채워놓습니다
#     csv['token'] = 0
#
#     # 분석에 있어서 의미가 없는 단어들은 제외합니다
#     # 바로 보였던 의미 없는 단어들 추가
#     stopwords = ['안녕', '잔', '수', '바람', '지금', 'ㅣ', '내', '뿐', '이것', '오늘', '재료', '요것', '양념', '우리', '주재료', '요리', '레시피',
#                  '숟가락', '입', '만', '개', '세상', '월', '년', '작년', '재작년', '때', '이번', '자료', '글']
#
#     for i in range(0, len(csv['des'])):
#         # csv 파일의 des, title, ing 열 안의 텍스트 명사 화
#         tmp = mecab.nouns(csv['des'][i])
#         tmp_title = mecab.nouns(csv['title'][i])
#         tmp_ing = mecab.nouns(csv['ing'][i])
#
#         tokens = []
#         # stopwords에 포함되지 않으면 tokens에 추가되는 방식
#         # tokens에 포함 여부 확인으로 중복 방지
#         for token in tmp:
#             if (not token in stopwords) and (not token in tokens):
#                 tokens.append(token)
#
#         for token in tmp_title:
#             if (not token in stopwords) and (not token in tokens):
#                 tokens.append(token)
#
#         for token in tmp_ing:
#             if (not token in stopwords) and (not token in tokens):
#                 tokens.append(token)
#
#                 # 이후 df['token'] 에다가 저장합니다
#         csv['token'][i] = tokens
with open("D:/sparta/ㅠㅠ/static/model/only_token.csv", 'rt', encoding='UTF8') as f:
    dr = csv.DictReader(f)
    s = pd.DataFrame(dr)
for i in range(len(s)):
    st = s['token'][i]
    list_str=st.split()
    s['token'][i]=list_str
def select_recipe(recipe_index, top_recipe,model):
        reccommend_id = []
        db_id = recipe_index - 1  # db에서 id가 1부터 시작하므로
        st=(s['token'][db_id])
        list_st=st[0].split()
        inferred_doc_vec = model.infer_vector(list_st)
        # df['token'][0] 의 숫자는 몇번 문서를 벡터와를 할지 설정해주는 숫자
        most_similar_docs = model.docvecs.most_similar([inferred_doc_vec], topn=top_recipe)
        for index, similarity in most_similar_docs:
            reccommend_id.append(index + 1)  # db에서 id가 1부터 시작하므로
        return reccommend_id[1:top_recipe]
def create_all(recipe_index, top_recipe):
    df = pd.read_table("D:/sparta/ㅠㅠ/static/model/rcp_data_tokenized.csv", sep=',')
    # df['token'] 에 담긴 토큰 형태의 문서를 tagged document 라는 데이터 형식으로 변환합니다
    print("a")
    documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(s['token'])]
    print("b")
    print(s['token'][5])
    model = Doc2Vec(documents, vector_size=30, window=7, epochs=5, min_count=0, workers=4)
    print("c")
    # model = tf.keras.models.load_model('D:/sparta/ㅠㅠ/static/model/iris.h5')
    totaldata=select_recipe(recipe_index,top_recipe,model)
    print("d")
    return totaldata
def main(request):
    user = request.user.is_authenticated
    like_list=tweetmodel.objects.filter(like=request.user).last()
    print(like_list)
    print("-------")
    print(like_list.id)
    l_list=create_all(like_list.id,5)
    print(l_list)
    final_list=[]
    for i in l_list:
        like_list = tweetmodel.objects.filter(id=i)
        final_list+= like_list
    print(final_list)
    if user:
        all_tweet = tweetmodel.objects.all()
        return render(request, 'main.html', {"tweet": all_tweet,"like":final_list})
    else:
        return redirect("/sign-in")
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
    user=request.user.username
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
        return render(request, 'detail.html',{"tweet": my_tweet,"tag":taglist,"comment": all_comment,"user":user})
    # , '
# @login_required  # 로그인이 되어있어야 실행가능
def write_comment(request, id):
    if request.method == "POST":
        T_comment = tweetcommant()
        T_comment.comment = request.POST.get("comment", '')  ##post로 name이 comment인 html의 요소안에서 텍스트를 가져온다
        # if T_comment.comment == '':
        #     return redirect(request, f"/detail/{id}",{"error":"글자를 적으시오"})
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
def comment_like(request,id):
    me =request.user
    click_rasi = tweetmodel.objects.get(id=id)
    if me in click_rasi.like.all():
        click_rasi.like.remove(request.user)
    else:
        click_rasi.like.add(request.user)
    return redirect(f'/detail/{id}')
def mypage(request):
    like=tweetmodel.objects.filter(like =request.user)
    td=[]
    for a in like:
        # like_count = tweetmodel.objects.filter(like=a.id)
        td+={a}
        # ff=[]
        # ff+={like_count}
        print("----------")
        # print(ff)
        print(td)
    return render(request, 'mypage.html',{"like": td})