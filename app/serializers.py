import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Info


class InfoSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Info
        fields = "__all__"









# class InfoModel:
#     """Створення класу для прикладу"""
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


# class InfoSerializer(serializers.Serializer):
#     """Серіалізатор для класу"""
#     title = serializers.CharField(max_length=225)
#     content = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     category_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Info.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get("title", instance.title)
#         instance.content = validated_data.get("content", instance.content)
#         instance.time_update = validated_data.get("time_update", instance.time_update)
#         instance.is_published = validated_data.get("is_published", instance.is_published)
#         instance.category_id = validated_data.get("category_id", instance.category_id)
#         instance.save()
#         return instance





# def encode():
#     """Кодування класу в джейсон"""
#     model = InfoModel('God of War', 'Content: God of War')
#     model_sr = InfoSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     """Декодування класу з джейсону"""
#     stream = io.BytesIO(b'{"title":"God of War", "content":"Content: God of War"}')
#     data = JSONParser().parse(stream)
#     serializer = InfoSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
