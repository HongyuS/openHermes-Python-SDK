# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ServiceAPIData"]


class ServiceAPIData(BaseModel):
    description: str
    """接口描述"""

    name: str
    """接口名称"""

    path: str
    """接口路径"""
