# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ServiceListParams"]


class ServiceListParams(TypedDict, total=False):
    created_by_me: Annotated[bool, PropertyInfo(alias="createdByMe")]
    """筛选我创建的"""

    favorited: bool
    """筛选我收藏的"""

    keyword: Optional[str]
    """搜索关键字"""

    page: int
    """页码"""

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """每页数量"""

    search_type: Annotated[Literal["all", "name", "description", "author"], PropertyInfo(alias="searchType")]
    """搜索类型"""
