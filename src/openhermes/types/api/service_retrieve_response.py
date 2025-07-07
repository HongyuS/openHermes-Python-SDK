# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .service_api_data import ServiceAPIData

__all__ = ["ServiceRetrieveResponse", "Result"]


class Result(BaseModel):
    name: str
    """服务名称"""

    service_id: str = FieldInfo(alias="serviceId")
    """服务 ID"""

    apis: Optional[List[ServiceAPIData]] = None
    """解析后的接口列表"""

    data: Optional[object] = None
    """YAML 内容数据对象"""


class ServiceRetrieveResponse(BaseModel):
    code: int

    message: str

    result: Result
    """GET /api/service/{serviceId} Result 数据结构"""
