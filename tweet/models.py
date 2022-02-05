from django.db import models
from user.models import UserModel

# Create your models here.

class tweetmodel(models.Model):
    # author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    r_id = models.CharField(max_length=9)
    url = models.CharField(max_length=45)
    tag = models.CharField(max_length=43)
    title = models.CharField(max_length=100)
    des = models.CharField(max_length=200)
    ing = models.CharField(max_length= 200)
    img_src = models.CharField(max_length= 100)

class tweetcommant(models.Model):
        class Meta:
            db_table = "comment"
        tweet = models.ForeignKey(tweetmodel, on_delete=models.CASCADE)
        # author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
        comment = models.CharField(max_length=256)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)


