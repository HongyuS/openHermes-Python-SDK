# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ServiceDeleteResponse", "Result"]


class Result(BaseModel):
    service_id: str = FieldInfo(alias="serviceId")
    """服务 ID"""


class ServiceDeleteResponse(BaseModel):
    code: int

    message: str

    result: Result
    """语义接口中心：基础服务操作 Result 数据结构"""
