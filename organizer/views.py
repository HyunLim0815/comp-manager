from django.http.response import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import APIView, api_view
from rest_framework.response import Response
from .forms import PerfectINFO
from .models import Org_info, Competition, com_judge, com_organizer, Judger
from .serializers import JudgerSerializer, Org_info_serializer, CompetitionSerializer, com_judge_serializer, com_organizer_serializer

# Create your views here.
class Org_info_list(APIView):
    '''
    列出所有Org_info实例或创建一个新的Org_info实例
    '''
    def get(self, request, format = None):
        info = Org_info.objects.all()
        serializer = Org_info_serializer(info, many = True)
        return Response(serializer.data)
    
    def post(self, request, format = None):
        serializer = Org_info_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
class Org_info_detail(APIView):
    
    '''
    检索、更新或删除一个Org_info实例
    '''
    def get_object(self, pk):
        try:
            return Org_info.objects.get(pk = pk)
        except Org_info.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format = None):
        org_info = self.get_object(pk)
        serializer = Org_info_serializer(org_info)
        return Response(serializer.data)
    
    def put(self, request, pk, format = None):
        org_info = self.get_object(pk)
        serializer = Org_info_serializer(org_info, data = request.data)
        if serializer.is_valid(pk):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format = None):
        org_info = self.get_object(pk)
        org_info.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
class Competitions(APIView):
    def get(self, request, format = None):
        com = Competition.objects.all()
        serializer = CompetitionSerializer(com, many = True)
        return Response(serializer.data)
    
    def post(self, request, format = None):
        serializer = CompetitionSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class CompetitionDeatil(APIView):
    def get_object(self, pk):
        try:
            return Competition.objects.get(pk = pk)
        except Competition.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format = None):
        com = self.get_object(pk)
        serializer = CompetitionSerializer(com)
        return Response(serializer.data)
    
    def put(self, request, pk, format = None):
        com = self.get_object(pk)
        serializer = CompetitionSerializer(com, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, fromat = None):
        com = self.get_object(pk)
        com.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class com_judge_list(APIView):
    def get(self, request, format = None):
        judge = com_judge.objects.all()
        serializer = com_judge_serializer(judge, many = True)
        return Response(serializer.data)
    
    def post(self, request, format = None):
        serializer = com_judge_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class com_judge_deatil(APIView):
    def get_object(self, pk):
        try:
            return com_judge.objects.get(pk = pk)
        except com_judge.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format = None):
        judge = self.get_object(pk)
        serializer = com_judge_serializer(judge)
        return Response(serializer.data)
    
    def put(self, request, pk, format = None):
        com = self.get_object(pk)
        serializer = CompetitionSerializer(com, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, fromat = None):
        com = self.get_object(pk)
        com.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class com_organizer_list(APIView):
    def get(self, request, format = None):
        org = com_organizer.objects.all()
        serializer = com_organizer_serializer(org, many = True)
        return Response(serializer.data)
    
    def post(self, request, format = None):
        serializer = com_organizer_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class com_organizer_detail(APIView):
    def get_object(self, pk):
        try:
            return com_organizer.objects.get(pk = pk)
        except com_organizer.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format = None):
        org = self.get_object(pk)
        serializer = com_organizer_serializer(org)
        return Response(serializer.data)
    
    def put(self, request, pk, format = None):
        org = self.get_object(pk)
        serializer = com_organizer_serializer(org, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, fromat = None):
        org = self.get_object(pk)
        org.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET','POST'])
def judgerlist(request):
    if request.method == 'GET':
        judgerlist = Judger.objects.all()
        serializer = JudgerSerializer(judgerlist, many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = JudgerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def judge_detail(request, pk):    
    try:
        detail = Judger.objects.get(pk = pk)
    except Judger.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = JudgerSerializer(detail)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = JudgerSerializer(detail, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def PerfectINFO(request):
    if request.method == 'POST':
        form = PerfectINFO(request.POST)
        if form.is_valid():
            return Response(status=status.HTTP_201_CREATED)
        else:
            form = PerfectINFO()
    elif request.method == "GET":
        return render(request, '/organizer/perfect_info.html', {'form': PerfectINFO})
    pass