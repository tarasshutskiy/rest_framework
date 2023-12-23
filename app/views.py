from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.response import Response

from .models import *
from .serializers import InfoSerializer
from rest_framework.views import APIView


# class InfoAPIView(generics.ListAPIView):
#     queryset = Info.objects.all()
#     serializer_class = InfoSerializer


class InfoAPIView(APIView):
    def get(self, request):
        info = Info.objects.all()
        return Response({'posts': InfoSerializer(info, many=True).data})

    def post(self, request):
        serializer = InfoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = Info.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            category_id=request.data['category_id']
        )
        return Response({'posts': InfoSerializer(post_new).data})
