from django.contrib import admin

# Register your models here.
from .models import Users, WX_users

admin.site.register(Users)
admin.site.register(WX_users)