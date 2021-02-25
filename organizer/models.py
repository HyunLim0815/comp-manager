from login.models import WX_users
from django.db import models
from django.db.models.deletion import CASCADE
# Create your models here.
types = [
    ('onLine', '线上'),
    ('offLine', '线下')
]

status_codes = [
    ('None','尚未开始'),
    ('St', '比赛开始'),
    ('Pa', '比赛暂停'),
    ('Sp', '比赛中止'),
    ('End', '比赛结束')
]

class Org_info(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=25)
    introduction = models.TextField(max_length=200)
    telephone = models.BigIntegerField()
    
class Competition(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=50)
    types = models.CharField(default='offLine', max_length=10)
    start = models.DateTimeField(editable=True, blank=False)
    end = models.DateTimeField(editable=True, blank=False)
    status = models.CharField(max_length=20, default='')
    rules = models.TextField(max_length=500)
    
class Judger(models.Model):
    user = models.ForeignKey(WX_users, on_delete=CASCADE)
    position = models.CharField(max_length=25)
    
class com_organizer(models.Model):
    com_id = models.ForeignKey(Competition, on_delete=CASCADE, primary_key=True)
    Organizer_id = models.ForeignKey(Org_info, on_delete=CASCADE)
      
class com_judge(models.Model):
    com_id = models.ForeignKey(Competition, on_delete=CASCADE, primary_key=True)
    Judge_id = models.ForeignKey(Judger, on_delete=CASCADE)