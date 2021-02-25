from team.models import Team
from rest_framework import serializers
from .models import user_info

class user_info_serializers(serializers.Serializer):
    id = serializers.CharField()
    stu_id = serializers.IntegerField()
    name = serializers.CharField()
    grade = serializers.CharField()
    _class = serializers.CharField()
    college = serializers.CharField()
    phone = serializers.CharField()
    
    def create(self, validated_data):
        return user_info.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.grade = validated_data.get('grade', instance.grade)
        instance.name = validated_data.get('name', instance.name)
        instance._class = validated_data.get('_class', instance._class)
        instance.college = validated_data.get('college', instance.college)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()
        return instance
    