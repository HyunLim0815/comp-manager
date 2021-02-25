# from rest_framework import serializers, status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Judger
# from .serializers import JudgerSerializer
# from django.shortcuts import render

# # Create your views here.
# @api_view(['GET','POST'])
# def judgerlist(request):
#     if request.method == 'GET':
#         judgerlist = Judger.objects.all()
#         serializer = JudgerSerializer(judgerlist, many = True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = JudgerSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['GET', 'PUT', 'DELETE'])
# def judge_detail(request, pk):
#     try:
#         detail = Judger.objects.get(pk = pk)
#     except Judger.DoesNotExist:
#         return Response(status = status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = JudgerSerializer(detail)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = JudgerSerializer(detail, data=request.data)
#         if serializer.is_valid():
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         detail.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)