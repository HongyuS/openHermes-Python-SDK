# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["AppFlowInfo"]


class AppFlowInfo(BaseModel):
    id: str
    """工作流 ID"""

    debug: bool
    """是否经过调试"""

    description: str
    """工作流简介"""

    name: str
    """工作流名称"""
