from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer, CreatePostSerializer

post_queryset_lookups = ["tags"]


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.prefetch_related(*post_queryset_lookups).all()
    serializer_class = PostSerializer

    @action(detail=False, methods=["POST"])
    def create_post(self, request, *args, **kwargs):
        serializer = CreatePostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            validated_data = serializer.data
            new_post = Post.objects.create(title=validated_data["title"], content=validated_data["content"])
            new_post.save()
            # TODO: Should set up a method to update the tags as well within this function
            return Response(data=validated_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
