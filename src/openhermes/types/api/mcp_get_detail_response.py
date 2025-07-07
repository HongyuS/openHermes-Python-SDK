# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .mcp_type import McpType
from ..._models import BaseModel

__all__ = ["McpGetDetailResponse", "Result", "ResultTool"]


class ResultTool(BaseModel):
    id: str
    """MCP 工具 ID"""

    description: str
    """MCP 工具描述"""

    input_schema: object
    """MCP 工具输入参数"""

    mcp_id: str
    """MCP ID"""

    name: str
    """MCP 工具名称"""


class Result(BaseModel):
    data: str
    """MCP 服务配置"""

    description: str
    """MCP 服务描述"""

    mcp_type: McpType = FieldInfo(alias="mcpType")
    """MCP 类型"""

    name: str
    """MCP 服务名称"""

    service_id: str = FieldInfo(alias="serviceId")
    """MCP 服务 ID"""

    icon: Optional[str] = None
    """图标"""

    is_active: Optional[bool] = FieldInfo(alias="isActive", default=None)
    """mcp 服务是否激活"""

    tools: Optional[List[ResultTool]] = None
    """MCP 服务 Tools 列表"""


class McpGetDetailResponse(BaseModel):
    code: int

    message: str

    result: Result
    """GET /api/mcp_service/{serviceId} Result 数据结构"""
