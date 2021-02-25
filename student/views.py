from django.http.response import Http404
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .models import user_info
from .serializers import user_info_serializers

# Create your views here.
class user_info_list(APIView):
    def get(self, request, format = None):
        u_info = user_info.objects.all()
        serializer = user_info_serializers(u_info, many = True)
        return Response(serializer.data)
    
    def post(self, request, format = None):
        serializer = user_info_serializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class user_info_detail(APIView):
    
    '''
    检索、更新或删除一个Org_info实例
    '''
    def get_object(self, pk):
        try:
            return user_info.objects.get(pk = pk)
        except user_info.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format = None):
        u_info = self.get_object(pk)
        serializer = user_info_serializers(u_info)
        return Response(serializer.data)
    
    def put(self, request, pk, format = None):
        u_info = self.get_object(pk)
        serializer = user_info_serializers(u_info, data = request.data)
        if serializer.is_valid(pk):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format = None):
        u_info = self.get_object(pk)
        u_info.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
