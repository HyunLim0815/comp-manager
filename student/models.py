from login.models import WX_users
from django.db import models
from django.db.models.deletion import CASCADE, SET_DEFAULT, SET_NULL
import sys 
sys.path.append("..") 


# Create your models here.
class user_info(models.Model):
    base_info = models.ForeignKey(WX_users, on_delete=CASCADE)
    stu_id = models.BigIntegerField(unique=True)
    grade = models.IntegerField(unique=False)
    _class = models.CharField(max_length=25)
    college = models.CharField(max_length=25)
    phone = models.BigIntegerField(unique=True)   