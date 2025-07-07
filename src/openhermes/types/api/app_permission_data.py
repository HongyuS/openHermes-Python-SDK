# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AppPermissionData"]


class AppPermissionData(BaseModel):
    authorized_users: Optional[List[str]] = FieldInfo(alias="authorizedUsers", default=None)
    """附加人员名单（如果可见性为部分人可见）"""

    visibility: Optional[Literal["protected", "public", "private"]] = None
    """可见性（public/private/protected）"""
