# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .response_data import ResponseData

__all__ = ["ServiceListResponse", "GetServiceListRsp", "GetServiceListRspResult", "GetServiceListRspResultService"]


class GetServiceListRspResultService(BaseModel):
    author: str
    """服务作者"""

    description: str
    """服务简介"""

    favorited: bool
    """是否已收藏"""

    icon: str
    """服务图标"""

    name: str
    """服务名称"""

    service_id: str = FieldInfo(alias="serviceId")
    """服务 ID"""


class GetServiceListRspResult(BaseModel):
    current_page: int = FieldInfo(alias="currentPage")
    """当前页码"""

    services: List[GetServiceListRspResultService]
    """解析后的服务列表"""

    total_count: int = FieldInfo(alias="totalCount")
    """总服务数"""


class GetServiceListRsp(BaseModel):
    code: int

    message: str

    result: GetServiceListRspResult
    """GET /api/service Result 数据结构"""


ServiceListResponse: TypeAlias = Union[GetServiceListRsp, ResponseData]
