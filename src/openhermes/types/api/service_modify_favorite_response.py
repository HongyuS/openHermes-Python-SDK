# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ServiceModifyFavoriteResponse", "Result"]


class Result(BaseModel):
    favorited: bool
    """是否已收藏"""

    service_id: str = FieldInfo(alias="serviceId")
    """服务 ID"""


class ServiceModifyFavoriteResponse(BaseModel):
    code: int

    message: str

    result: Result
    """PUT /api/service/{serviceId} Result 数据结构"""
