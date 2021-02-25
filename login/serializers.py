from rest_framework import serializers
from .models import *
class WX_user_Serializer(serializers.Serializer):
    # 将模型的字段改写成serializers对应的Field
    WX_id = serializers.CharField()
    telephone = serializers.CharField()

    # 根据验证过的数据创建并返回一个新的实例
    def creat_user(self, data):
        return WX_users.objects.create(**data)
    
    # 根据提供的验证过的数据更新和返回一个已存在的实例
    def update(self,instance, data):
        instance.WX_id = data.get('WX_id', instance.WX_id) 
        instance.telephone = data.get('telephone', instance.telephone)
        instance.save()
        return instance
