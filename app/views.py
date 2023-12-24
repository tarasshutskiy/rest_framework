from django.forms import model_to_dict
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import *
from .serializers import InfoSerializer
from rest_framework.views import APIView


class InfoViewSet(viewsets.ModelViewSet):
    # queryset = Info.objects.all()
    serializer_class = InfoSerializer

    """Створення нестандартних маршрутів для - категорії"""
    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Info.objects.all()[:3]
        return Info.objects.filter(pk=pk)




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