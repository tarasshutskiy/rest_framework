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
        lst = Info.objects.all().values()
        return Response({'posts': list(lst)})

    def post(self, request):
        post_new = Info.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            category_id=request.data['category_id']
        )
        return Response({'posts': model_to_dict(post_new)})
