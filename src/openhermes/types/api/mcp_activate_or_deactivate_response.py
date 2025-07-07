# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .base_mcp_service_operation import BaseMcpServiceOperation

__all__ = ["McpActivateOrDeactivateResponse"]


class McpActivateOrDeactivateResponse(BaseModel):
    code: int

    message: str

    result: BaseMcpServiceOperation
    """插件中心：MCP 服务操作 Result 数据结构"""
