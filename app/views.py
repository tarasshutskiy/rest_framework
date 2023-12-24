from django.forms import model_to_dict
from rest_framework import generics, viewsets
from rest_framework.response import Response

from .models import *
from .serializers import InfoSerializer
from rest_framework.views import APIView


class InfoViewSet(viewsets.ModelViewSet):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer





"""BASE GENERICS APIVIEWS"""
# class InfoAPIList(generics.ListCreateAPIView):
#     queryset = Info.objects.all()
#     serializer_class = InfoSerializer
#
#
# class InfoAPIUpdate(generics.UpdateAPIView):
#     queryset = Info.objects.all()
#     serializer_class = InfoSerializer
#
#
# class InfoAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Info.objects.all()
#     serializer_class = InfoSerializer












"""BASE FUNCTION WE CAN CREATED"""
# class InfoAPIView(APIView):
#     def get(self, request):
#         info = Info.objects.all()
#         return Response({'posts': InfoSerializer(info, many=True).data})
#
#     def post(self, request):
#         serializer = InfoSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'posts': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#         try:
#             instance = Info.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
#
#         serializer = InfoSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'posts': serializer.data})
#
#
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#         try:
#             instance = Info.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
#
#         instance.delete()
#         return Response({'post': "delete post" + str(pk)})