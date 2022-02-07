import csv
import pandas as pd
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Mamison_team10.settings")

import django
django.setup()
from tweet.models import tweetmodel
with open('../static/model/rcp_data_v5.csv','rt',encoding='UTF8') as f:
    dr = csv.DictReader(f)
    s = pd.DataFrame(dr)
ss = []
for i in range(len(s)):
    st = (s['id'][i], s['url'][i], s['tag'][i], s['title'][i], s['des'][i], s['ing'][i], s['img_src'][i])
    ss.append(st)
for i in range(len(s)):
    tweetmodel.objects.create(r_id=ss[i][0], url=ss[i][1], tag=ss[i][2], title=ss[i][3], des=ss[i][4], ing=ss[i][5], img_src=ss[i][6])