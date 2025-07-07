# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ServiceUpdateParams"]


class ServiceUpdateParams(TypedDict, total=False):
    data: Required[object]
    """对应 YAML 内容的数据对象"""

    service_id: Annotated[Optional[str], PropertyInfo(alias="serviceId")]
    """服务 ID（更新时传递）"""
