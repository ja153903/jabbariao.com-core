import logging

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request

from .mixins import PostTagMixin
from .models import Post
from .serializers import PostSerializer, CreatePostSerializer

logger = logging.getLogger(__name__)

post_queryset_lookups = ["tags"]


class PostViewSet(PostTagMixin, viewsets.ModelViewSet):
    queryset = Post.objects.prefetch_related(*post_queryset_lookups).all()
    serializer_class = PostSerializer

    @action(detail=False, methods=["POST"])
    def create_post(self, request: Request) -> Response:
        serializer = CreatePostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            validated_data = serializer.data
            new_post = Post.objects.create(title=validated_data["title"], content=validated_data["content"])

            if "tags" in validated_data:
                self.add_tags_to_post(new_post, validated_data["tags"])

            new_post.save()

            logger.info(f"[/api/posts/create_post]: Created post with id #{new_post.id} at {new_post.created}")

            return Response(data=validated_data, status=status.HTTP_201_CREATED)

        logger.error("[/api/posts/create_post]: Failed to create a new post")

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
