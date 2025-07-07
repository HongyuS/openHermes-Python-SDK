# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from .app_type import AppType

__all__ = ["AppListParams"]


class AppListParams(TypedDict, total=False):
    app_type: Annotated[Optional[AppType], PropertyInfo(alias="appType")]
    """应用类型"""

    created_by_me: Annotated[bool, PropertyInfo(alias="createdByMe")]
    """筛选我创建的"""

    favorited: bool
    """筛选我收藏的"""

    keyword: Optional[str]
    """搜索关键字"""

    page: int
    """页码"""
