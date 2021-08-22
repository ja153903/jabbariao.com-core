from typing import List

from .models import Post, Tag


class PostTagMixin:
    def add_tags_to_post(self, post: Post, tags: List[str]):
        if not tags:
            return

        for tag in tags:
            current_tag, _ = Tag.objects.get_or_create(name=tag)
            post.tags.add(current_tag)

        post.save()
