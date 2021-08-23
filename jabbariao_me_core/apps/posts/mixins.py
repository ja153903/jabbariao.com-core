import logging
from typing import List

from django.db.models import Q

from .models import Post, Tag

logger = logging.getLogger(__name__)


class PostTagMixin:
    def add_tags_to_post(self, post: Post, tags: List[str]) -> None:
        if not tags:
            return

        for tag in tags:
            current_tag, _ = Tag.objects.get_or_create(name=tag)
            post.tags.add(current_tag)

        post.save()

        logger.info(f"[PostTagMixin::add_tags_to_post]: Added {len(tags)} tags ({tags}) to post with id # {post.id}")

    def update_tags_for_post(self, post: Post, tags: List[str]) -> None:
        if not tags:
            return

        name_not_in_list = ~Q(name__in=tags)

        # Delete any tags that are not in the current list
        post.tags.filter(name_not_in_list).delete()

        updated_tags = []

        for tag in tags:
            if not post.tags.filter(name=tag).exists():
                updated_tags.append(tag)

        self.add_tags_to_post(post, updated_tags)
