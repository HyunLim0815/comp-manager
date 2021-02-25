from django.contrib import admin
from .models import Org_info, com_judge, com_organizer, Competition, Judger
# Register your models here.
admin.site.register([Org_info, Competition, com_judge, com_organizer, Judger])