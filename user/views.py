from django.shortcuts import render
import requests
import pandas as pd
# from newspaper import Article
from bs4 import BeautifulSoup


# Create your views here.

def intro_view(request):
    return render(request, 'intro.html')


def sign_in_view(request):
    return render(request, 'user/signin.html')


# ###크롤링을 위한 정보
#
# def make_urllist(page_num, way, situation,material, kind):
#   urllist = []
#   for i in range(1, page_num + 1):
#     url = f'https://www.10000recipe.com/recipe/list.html?cat1={way}&cat2={situation}&cat3={material}&cat4={kind}&order=reco&page={i}'
#     print(url)
#     # 헤더를 붙여서
#     headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}
#
#     # 리퀘스트 요청을 보냄
#     resipis = requests.get(url, headers=headers)
#
#     # html 파싱을 위한 객체 생성
#     soup = BeautifulSoup(resipis.content, 'html.parser')
#
#     #contents_area_full > ul > ul > li:nth-child(1) > div.common_sp_thumb > a
#     # ul 태그가 2개인데 그 중에 첫번째 것을 select
#     resipis_list = soup.select('.common_sp_list_ul > li')
#     #contents_area_full > ul > ul > li:nth-child(2) > div.common_sp_thumb > a
#     #contents_area_full > ul > ul > li:nth-child(2) > div.common_sp_thumb > a
#     # 두번째 것을 select 할것이 없으므로 주석처리
#     # news_list.extend(soup.select('.type06 li dl'))
#     ################################################
#
#     # urllist 에 a 태그 내부의 href 내용 (기사 별 url 링크) 을 추가!
#     for line in resipis_list:
#       # templine = line.select_one('div.common_sp_thumb')
#       tempimglink = line.select_one(' div.common_sp_thumb > a')['href']
#       imglink = f'https://www.10000recipe.com/{tempimglink}'
#       urllist.append(imglink)
#   return urllist


# idx2way = { ' ' : '전체' , '63' : '밑반찬' ,  '56' : '메인반찬 ' , '54' : '국/탕' , '55' : '찌개' , '60' : '디저트' , '53' : '면/만두' , '52' : '밥/죽/떡' , '61' : '퓨전' , '57' : '김치/젓갈/장류' , '58' : '양념/소스/잼' , '65' : '양식' , '64' : '셀러드' , '68' : '스프' , '66' : '빵' , '69' : '과자' , '59' : '차/음료/술' , '62' : '기타' }
# idx2situation = {' ' : '전체' , '12' : '일상' , '12' : '일상' , '18' : '초스피드' , '13' : '손님접대' , '19' : '술안주' , '21' : '다이어트' , '15' : '도시락' , '43' : '영양식' , '17' : '간식' , '45' : '야식' , '20' : '푸드스타일링' , '46' : '해장' , '44' : '명절' , '14' : '이유식' , '22' : '기타' }
# idx2material = {' ' : '전체' ,  '70' : '소고기' , '71' : '돼지고기' , '72' : '닭고기' , '23' : '육류' , '28' : '채소류' , '24' : '해물류' , '50' : '달걀/유제품' , '33' : '가공식품류' , '47' : '쌀' , '32' : '밀가루' , '25' : '건어물류' , '31' : '버섯류' , '48' : '과일류' , '27' : '콩/견과류' , '26' : '곡류' , '34' : '기타' }
# idx2kind ={' ' : '전체' , '6' : '볶음' , '1' : '끓이기' , '7' : '부침' , '36' : '조림' , '41' : '무침' , '42' : '비빔' , '8' : '찜' , '10' : '절임' , '9' : '튀김' , '38' : '삶기' , '67' : '굽기' , '39' : '데치기' , '37' : '회' , '11' : '기타'}
#

# def make_data(urllist, code1,code2,code3,code4):
#   text_list = []
#
#   # 각 기사 별 Url 이 urllist 에 담겨있으니,
#   # Article 이라는 newspaper3k 내부 함수를 이용해서 크롤링 진행
#   for url in urllist:
#     article = Article(url, language='ko')
#     article.download()
#     article.parse()
#     # article.text 는 본문 // 제목을 가져오고 싶다면 article.title
#     text_list.append(article.text)
#
#   # news 라는 열에다가 기사 본문을 추가해서 데이터프레임 생성
#   df = pd.DataFrame({'news': text_list})
#   # code 라는 열에다가는 기사 카테고리 추가
#   df['code'] = idx2word[str(code)]
#   return df

def sign_up_view(request):
    # urllist = []
    # imglist =[]
    # for i in range(1, 1 + 1):
    #   url = f'https://www.10000recipe.com/recipe/list.html?cat1=6&cat2=12&cat3=70&cat4=63&order=reco&page=2'
    #   print(url)
    #   # 헤더를 붙여서
    #   headers = {
    #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}
    #
    #   # 리퀘스트 요청을 보냄
    #   resipis = requests.get(url, headers=headers)
    #
    #   # html 파싱을 위한 객체 생성
    #   soup = BeautifulSoup(resipis.content, 'html.parser')
    #
    #   # contents_area_full > ul > ul > li:nth-child(1) > div.common_sp_thumb > a
    #   # ul 태그가 2개인데 그 중에 첫번째 것을 select
    #   resipis_list = soup.select('.common_sp_list_ul > li')
    #   # contents_area_full > ul > ul > li:nth-child(2) > div.common_sp_thumb > a
    #   # contents_area_full > ul > ul > li:nth-child(2) > div.common_sp_thumb > a
    #   # 두번째 것을 select 할것이 없으므로 주석처리
    #   # news_list.extend(soup.select('.type06 li dl'))
    #   ################################################
    #
    #   # urllist 에 a 태그 내부의 href 내용 (기사 별 url 링크) 을 추가!
    #   for line in resipis_list:
    #     # templine = line.select_one('div.common_sp_thumb')
    #     tempimglink = line.select_one(' div.common_sp_thumb > a')['href']
    #     imglink = f'https://www.10000recipe.com/{tempimglink}'
    #     urllist.append(imglink)
    #     tempimglist =line.select_one('a.common_sp_link > img')['src']
    #     alllist =[]
    #     alldic = {'imglink': urllist, 'imgs' : tempimglist}
    #     alllist.append(alldic)
    #     print (alllist)
    return render(request, 'user/signup.html')
