# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["McpCreateOrUpdateResponse", "Result"]


class Result(BaseModel):
    name: str
    """MCP 服务名称"""

    service_id: str = FieldInfo(alias="serviceId")
    """MCP 服务 ID"""


class McpCreateOrUpdateResponse(BaseModel):
    code: int

    message: str

    result: Result
    """插件中心：MCP 服务属性数据结构"""
