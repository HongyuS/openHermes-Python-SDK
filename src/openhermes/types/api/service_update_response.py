# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .service_api_data import ServiceAPIData

__all__ = ["ServiceUpdateResponse", "Result"]


class Result(BaseModel):
    apis: List[ServiceAPIData]
    """解析后的接口列表"""

    name: str
    """服务名称"""

    service_id: str = FieldInfo(alias="serviceId")
    """服务 ID"""


class ServiceUpdateResponse(BaseModel):
    code: int

    message: str

    result: Result
    """语义接口中心：服务属性数据结构"""
