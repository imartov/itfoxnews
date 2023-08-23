from rest_framework import serializers
from .models import *


class NewsPostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = NewsPost
        fields = "__all__"   
