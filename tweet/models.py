from django.db import models

# Create your models here.

class tweetmodel(models.Model):
    r_id = models.CharField(max_length=9)
    url = models.CharField(max_length=45)
    tag = models.CharField(max_length=43)
    title = models.CharField(max_length=100)
    des = models.CharField(max_length=200)
    ing = models.CharField(max_length= 200)
    img_src = models.CharField(max_length= 100)
