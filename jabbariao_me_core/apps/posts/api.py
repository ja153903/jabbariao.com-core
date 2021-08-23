import logging

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request

from .mixins import PostTagMixin
from .models import Post
from .serializers import PostSerializer, CreatePostSerializer, UpdatePostSerializer

logger = logging.getLogger(__name__)

post_queryset_prefetch_related_lookups = ["tags"]


class PostViewSet(PostTagMixin, viewsets.ModelViewSet):
    queryset = Post.objects.prefetch_related(*post_queryset_prefetch_related_lookups).all()
    serializer_class = PostSerializer

    @action(detail=False, methods=["POST"])
    def create_post(self, request: Request) -> Response:
        serializer = CreatePostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            validated_data = serializer.validated_data
            new_post = Post.objects.create(title=validated_data["title"], content=validated_data["content"])

            if "tags" in validated_data:
                self.add_tags_to_post(new_post, validated_data["tags"])

            new_post.save()

            logger.info(f"[/api/posts/create_post]: Created post with id #{new_post.id} at {new_post.created}")

            return Response(data=validated_data, status=status.HTTP_201_CREATED)

        logger.info("[/api/posts/create_post]: Failed to create a new post")

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["PATCH"])
    def update_post(self, request, pk) -> Response:
        post = self.get_object()

        serializer = UpdatePostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            for key, value in serializer.validated_data.items():
                if key == "tags":
                    # Assume that for updating tags that we are given all tags
                    # that exist on the post
                    self.update_tags_for_post(post, value)
                else:
                    setattr(post, key, value)

            post.save()

            logger.info(f"[/api/posts/update_post/{pk}]: Updated post with id #{pk}")

            output_serializer_data = PostSerializer(post).data

            return Response(data=output_serializer_data, status=status.HTTP_200_OK)

        logger.info(f"[/api/posts/update_post/{pk}]: Failed to update post with id #{pk}")

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
