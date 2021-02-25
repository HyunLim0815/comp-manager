from django.contrib import admin
from .models import Team, com_score, com_team, Student
# Register your models here.
admin.site.register([Team, com_team, com_score, Student])