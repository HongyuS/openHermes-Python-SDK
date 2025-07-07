# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .response_data import ResponseData

__all__ = [
    "McpGetListResponse",
    "GetMcpServiceListRsp",
    "GetMcpServiceListRspResult",
    "GetMcpServiceListRspResultService",
]


class GetMcpServiceListRspResultService(BaseModel):
    author: str
    """mcp 服务作者"""

    description: str
    """mcp 服务简介"""

    icon: str
    """mcp 服务图标"""

    mcpservice_id: str = FieldInfo(alias="mcpserviceId")
    """mcp 服务 ID"""

    name: str
    """mcp 服务名称"""

    is_active: Optional[bool] = FieldInfo(alias="isActive", default=None)
    """mcp 服务是否激活"""

    status: Optional[Literal["installing", "ready", "failed"]] = None
    """mcp 服务状态"""


class GetMcpServiceListRspResult(BaseModel):
    current_page: int = FieldInfo(alias="currentPage")
    """当前页码"""

    services: List[GetMcpServiceListRspResultService]
    """解析后的服务列表"""

    total_count: int = FieldInfo(alias="totalCount")
    """总服务数"""


class GetMcpServiceListRsp(BaseModel):
    code: int

    message: str

    result: GetMcpServiceListRspResult
    """GET /api/service Result 数据结构"""


McpGetListResponse: TypeAlias = Union[GetMcpServiceListRsp, ResponseData]
