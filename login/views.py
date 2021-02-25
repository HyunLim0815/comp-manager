from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import WX_user_Serializer


     
@api_view(['GET','POST'])
def login_api_list(request):
    #列出所有的对象或创建一个新的对象
    if request.method == 'POST':
        serializer = WX_user_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    pass

@api_view(['GET', 'PUT', 'DELETE'])
def login_api_detail(request, id):
    try:
        WX_user = WX_users.objects.get(id = id)
    except WX_users.DoesNotExist :
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = WX_user_Serializer(WX_user)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = WX_user_Serializer(WX_user,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        WX_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    