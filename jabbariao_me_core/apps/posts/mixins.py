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
        """
        This function takes a Post instance and a list of tags.
        This list of tags comes from an HTTP request body.
        To update the tags for a post, we take the set difference
        of the tags that we got from the request from the tags
        that exist on the post instance.

        We then add the intersection from those two sets to the
        updated set of tags.

        We then clear the current tags on the post and use the
        function above to add the updated tags to the post.
        """
        if not tags:
            return

        tags = set(tags)
        current_tags = set(post.tags.all())

        # (B - A) + (B ^ A)
        updated_tags = tags.difference(current_tags)
        updated_tags.update(tags.intersection(current_tags))

        post.tags.clear()

        self.add_tags_to_post(post, list(updated_tags))
