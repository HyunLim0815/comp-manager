import os
from django.db import models
from django.db.models.deletion import CASCADE
import sys 
sys.path.append("..") 
from organizer.models import Competition, Judger
from student.models import user_info
from 大学生比赛评分项目 import settings
# Create your models here.

def upload_dir(com_id, name):
    com_id = Competition.id
    name = name
    media_dir = settings.MEDIA_ROOT
    path = media_dir + str(com_id) + '\\' + str(name)
    os.makedirs(path)
    return path

class Team(models.Model):    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10, unique=True)
    competition_id = models.ForeignKey(Competition, on_delete=CASCADE)
    groups = models.CharField(max_length=25)
    works = models.FileField(upload_to=settings.MEDIA_ROOT+str(name), null=True, blank=True)
    stu_id = models.ForeignKey(user_info, on_delete=CASCADE, default='11111')
    
class com_team(models.Model):
    com_id = models.ForeignKey(Competition, on_delete=CASCADE, primary_key=True)
    Team_id = models.ForeignKey(Team,on_delete=CASCADE)    
    
class com_score(models.Model):
    judge_id = models.ForeignKey(Judger, on_delete=CASCADE)
    team_id = models.ForeignKey(Team, on_delete=CASCADE)
    scores = models.CharField(max_length=5) 
    
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    info_id = models.ForeignKey(user_info, on_delete=CASCADE)
    team_id = models.ForeignKey(Team,on_delete=CASCADE) 