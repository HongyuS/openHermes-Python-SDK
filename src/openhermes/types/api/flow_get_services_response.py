# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FlowGetServicesResponse", "Result", "ResultService", "ResultServiceNodeMetaData"]


class ResultServiceNodeMetaData(BaseModel):
    call_id: str = FieldInfo(alias="callId")

    created_at: Optional[float] = FieldInfo(alias="createdAt", default=None)

    description: str

    name: str

    node_id: str = FieldInfo(alias="nodeId")

    parameters: Optional[object] = None

    editable: Optional[bool] = None


class ResultService(BaseModel):
    name: str
    """服务名称"""

    service_id: str = FieldInfo(alias="serviceId")
    """服务 ID"""

    type: str
    """服务类型"""

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)
    """创建时间"""

    node_meta_datas: Optional[List[ResultServiceNodeMetaData]] = FieldInfo(alias="nodeMetaDatas", default=None)


class Result(BaseModel):
    services: Optional[List[ResultService]] = None
    """服务列表"""


class FlowGetServicesResponse(BaseModel):
    code: int

    message: str

    result: Result
    """GET /api/flow/service result"""
