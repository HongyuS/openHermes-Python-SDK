# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AppModifyFavoriteParams"]


class AppModifyFavoriteParams(TypedDict, total=False):
    favorited: Required[bool]
    """是否收藏"""
