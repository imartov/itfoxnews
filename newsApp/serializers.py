from rest_framework import serializers
from .models import *


class NewsPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPost
        fields = "__all__"   
    
       #  date_create = serializers.DateTimeField()
   #  date_update = serializers.DateTimeField()
   #  title = serializers.CharField(max_length=255)
   #  text = serializers.CharField()
   #  author = serializers.StringRelatedField()

   #  def create(self, validated_data):
   #      return NewsPost.objects.create(**validated_data)

   #  def update(self, instance, validated_data):
   #     instance.date_create = validated_data.get('date_create', instance.date_create)
   #     instance.date_update = validated_data.get('date_update', instance.date_update)
   #     instance.title = validated_data.get('title', instance.title)
   #     instance.text = validated_data.get('text', instance.text)
   #     instance.author = validated_data.get('author', instance.author)

   #     instance.save()
   #     return instance