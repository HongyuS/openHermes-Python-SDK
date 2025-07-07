# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .comment_type import CommentType

__all__ = ["APIAddCommentParams"]


class APIAddCommentParams(TypedDict, total=False):
    comment: Required[CommentType]
    """点赞点踩类型"""

    group_id: Required[str]

    record_id: Required[str]

    dislike_reason: str

    reason_description: str

    reason_link: str
