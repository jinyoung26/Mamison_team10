import csv
import pandas as pd
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Mamison_team10.settings")
import django
django.setup()
from tweet.models import tweetmodel
from user.models import  UserModel
with open('../static/model/rcp_data_8888_v66.csv','rt',encoding='UTF8') as f:
    dr = csv.DictReader(f)
    s = pd.DataFrame(dr)
ss = []
user=UserModel.objects.get(username="bbb6045")
for i in range(len(s)):
    st = (s['id'][i], s['url'][i], s['tag'][i],s['food'][i], s['title'][i], s['des'][i], s['ing'][i], s['img_src'][i])
    ss.append(st)
for i in range(len(s)):
    tweetmodel.objects.create( author=user ,r_id=ss[i][0], url=ss[i][1], tag=ss[i][2],food=ss[i][3], title=ss[i][4], des=ss[i][5], ing=ss[i][6], img_src=ss[i][7])