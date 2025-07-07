# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AppLinkParam"]


class AppLinkParam(TypedDict, total=False):
    title: Required[str]
    """链接标题"""

    url: Required[str]
    """链接地址"""
