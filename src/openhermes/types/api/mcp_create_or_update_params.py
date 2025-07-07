# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .mcp_type import McpType

__all__ = ["McpCreateOrUpdateParams"]


class McpCreateOrUpdateParams(TypedDict, total=False):
    config: Required[str]
    """MCP 服务配置"""

    description: Required[str]
    """MCP 服务描述"""

    name: Required[str]
    """MCP 服务名称"""

    icon: str
    """图标"""

    mcp_type: Annotated[McpType, PropertyInfo(alias="mcpType")]
    """MCP 传输协议(Stdio/SSE/Streamable)"""

    service_id: Annotated[Optional[str], PropertyInfo(alias="serviceId")]
    """服务 ID（更新时传递）"""
