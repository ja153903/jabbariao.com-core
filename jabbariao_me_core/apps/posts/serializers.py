from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class CreatePostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=256, required=True, allow_blank=False)
    content = serializers.CharField(required=False, allow_blank=True)
    tags = serializers.ListField(child=serializers.CharField(required=False, allow_blank=True), allow_empty=True)
