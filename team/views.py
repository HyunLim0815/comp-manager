from django.http.response import Http404
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .models import Team, com_team, com_score, Student
from .serializers import StudentSerializers, TeamSerializers, com_score_serializer, com_team_serializer
from django.shortcuts import render

# Create your views here.
class TeamList(APIView):
    def get(self, request, format = None):
        team = Team.objects.all()
        serializer = TeamSerializers(team, many = True)
        return Response(serializer.data)
    
    def post(self, request, format = None):
        serializer = TeamSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class TeamDeatil(APIView):
    def get_object(self, pk):
        try:
            return Team.objects.get(pk = pk)
        except Team.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format = None):
        team = self.get_object(pk)
        serializer = TeamSerializers(team)
        return Response(serializer.data)
    
    def put(self, request, pk, format = None):
        team = self.get_object(pk)
        serializer = TeamSerializers(team, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, fromat = None):
        team = self.get_object(pk)
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class com_team_list(APIView):
    def get(self, request, format = None):
        team = com_team.objects.all()
        serializer = com_team_serializer(team, many = True)
        return Response(serializer.data)
    
    def post(self, request, format = None):
        serializer = com_team_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class com_team_detail(APIView):
    def get_object(self, pk):
        try:
            return com_team.objects.get(pk = pk)
        except com_team.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format = None):
        team = self.get_object(pk)
        serializer = com_team_serializer(team)
        return Response(serializer.data)
    
    def put(self, request, pk, format = None):
        team = self.get_object(pk)
        serializer = com_team_serializer(team, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, fromat = None):
        team = self.get_object(pk)
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class com_scroe_list(APIView):
    def get(self, request, format = None):
        score = com_score.objects.all()
        serializer = com_score_serializer(score, many = True)
        return Response(serializer.data)
    
    def post(self, request, format = None):
        serializer = com_score_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class com_scroe_detail(APIView):
    def get_object(self, pk):
        try:
            return com_score.objects.get(pk = pk)
        except com_score.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format = None):
        score = self.get_object(pk)
        serializer = com_score_serializer(score)
        return Response(serializer.data)
    
    def put(self, request, pk, format = None):
        score = self.get_object(pk)
        serializer = com_score_serializer(score, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, fromat = None):
        score = self.get_object(pk)
        score.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StudentList(APIView):
    def get(self, request, format = None):
        stu = Student.objects.all()
        serializer = StudentSerializers(stu, many = True)
        return Response(serializer.data)
    
    def post(self, request, format = None):
        serializer = StudentSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class StudentDeatil(APIView):
    def get_object(self, pk):
        try:
            return Student.objects.get(pk = pk)
        except Student.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format = None):
        stu = self.get_object(pk)
        serializer = StudentSerializers(stu)
        return Response(serializer.data)
    
    def put(self, request, pk, format = None):
        stu = self.get_object(pk)
        serializer = StudentSerializers(stu, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, fromat = None):
        stu = self.get_object(pk)
        stu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
