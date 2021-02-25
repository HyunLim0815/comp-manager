from rest_framework import serializers
from django.utils import timezone
from .models import Judger, Org_info, Competition, com_judge, com_organizer

class Org_info_serializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField()
    introduction = serializers.CharField(allow_blank = False, max_length = 200)
    telephone = serializers.CharField(allow_blank = False)
    def create(self, validated_data):
        return Org_info.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.introduction = validated_data.get('introduction', instance.introduction)
        instance.telephone = validated_data.get('telephone', instance.telephone)
        instance.save()
        return instance

class CompetitionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField()
    types = serializers.CharField(default = 'offLine')
    start = serializers.DateTimeField(default_timezone=timezone.now())
    end = serializers.DateTimeField()
    status = serializers.CharField(default = 'None')
    rules = serializers.CharField()
    def create(self, validated_data):
        return Competition.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.rules = validated_data.get('rules', instance.rules)
        instance.save()
        return instance

class com_judge_serializer(serializers.Serializer):
    com_id = serializers.IntegerField()
    judge_id = serializers.IntegerField()
    def create(self, validated_data):
        return com_judge.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.judge_id = validated_data.get('judge_id', instance.judge_id)
        instance.save()
        return instance
    
class com_organizer_serializer(serializers.Serializer):
    com_id = serializers.IntegerField()
    org_id = serializers.IntegerField()
    def create(self, validated_data):
        return com_organizer.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.org_id = validated_data.get('org_id', instance.org_id)
        instance.save()
        return instance

class JudgerSerializer(serializers.Serializer):
    judger = serializers.IntegerField()
    position = serializers.CharField()
    def create(self, validated_data):
        return Judger.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.judger = validated_data.get('judger',instance.judger)
        instance.position = validated_data.get('position', instance.position)
        return instance
    
    