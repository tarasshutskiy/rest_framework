from rest_framework import generics
from .models import *
from .serializers import InfoSerializer


class InfoAPIView(generics.ListAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer

