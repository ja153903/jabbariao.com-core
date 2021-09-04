from rest_framework import serializers

from .models import Post, Comment


# Output Serializers
class TagSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = ("id", "title", "content", "created", "updated", "tags", "comments")


# Input Serializers (for validation)
class CreatePostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=256, required=True, allow_blank=False)
    content = serializers.CharField(required=False, allow_blank=True)
    tags = serializers.ListField(child=serializers.CharField(required=False, allow_blank=True), allow_empty=True)


class UpdatePostSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    content = serializers.CharField(required=False, allow_blank=True)
    tags = serializers.ListField(child=serializers.CharField(required=False))
