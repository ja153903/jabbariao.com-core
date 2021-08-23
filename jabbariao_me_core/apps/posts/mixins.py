import logging
from typing import List

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

        tags = set(tags)
        current_tags = set(post.tags.all())

        # (B - A) + (B ^ A)
        updated_tags = tags.difference(current_tags)
        updated_tags.update(tags.intersection(current_tags))

        self.add_tags_to_post(post, list(updated_tags))
