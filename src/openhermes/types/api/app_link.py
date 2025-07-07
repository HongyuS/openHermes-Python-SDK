# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["AppLink"]


class AppLink(BaseModel):
    title: str
    """链接标题"""

    url: str
    """链接地址"""
