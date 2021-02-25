from rest_framework import serializers
from .models import Team, com_score, com_team, Student

class TeamSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField()
    competition_id = serializers.IntegerField()
    groups = serializers.CharField()
    works = serializers.FileField()
    stu_id_1 = serializers.IntegerField()
    stu_id_2 = serializers.IntegerField()
    stu_id_3 = serializers.IntegerField()
    stu_id_4 = serializers.IntegerField()
    stu_id_5 = serializers.IntegerField()
    stu_id_6 = serializers.IntegerField()
    
    def create(self, validated_data):
        return Team.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.competition_id = validated_data.get('competition_id', instance.competition_id)
        instance.groups = validated_data.get('groups', instance.groups)
        instance.works = validated_data.get('work', instance.works)
        instance.stu_id_1 = validated_data.get('stu_id_1', instance.stu_id_1)
        instance.stu_id_2 = validated_data.get('stu_id_2', instance.stu_id_2)
        instance.stu_id_3 = validated_data.get('stu_id_3', instance.stu_id_3)
        instance.stu_id_4 = validated_data.get('stu_id_4', instance.stu_id_4)
        instance.stu_id_5 = validated_data.get('stu_id_5', instance.stu_id_6)
        instance.stu_id_6 = validated_data.get('stu_id_6', instance.stu_id_6)
        instance.save()
        return instance 

class com_score_serializer(serializers.Serializer):
    judge_id = serializers.IntegerField()
    team_id = serializers.IntegerField()
    scores = serializers.CharField()
    def create(self, validated_data):
        return com_score.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.scores = validated_data.get('scores')
        return instance
          
class com_team_serializer(serializers.Serializer):
    com_id = serializers.IntegerField()
    team_id = serializers.IntegerField()
    def create(self, validated_data):
        return com_team.objects.create(**validated_data)
    pass

class StudentSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    info_id = serializers.IntegerField()
    team_id = serializers.IntegerField()
    
    def create(self, validated_data):
        return Student.objects.create(validated_data)
    
    def update(self, instance, validated_data):
        instance.team_id = validated_data.get('team_id', instance.team_id)
        instance.save()
        return instance
    