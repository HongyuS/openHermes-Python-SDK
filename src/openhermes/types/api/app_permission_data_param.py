# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AppPermissionDataParam"]


class AppPermissionDataParam(TypedDict, total=False):
    authorized_users: Annotated[Optional[List[str]], PropertyInfo(alias="authorizedUsers")]
    """附加人员名单（如果可见性为部分人可见）"""

    visibility: Literal["protected", "public", "private"]
    """可见性（public/private/protected）"""
