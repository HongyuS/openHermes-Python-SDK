# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .position_item import PositionItem

__all__ = ["NodeItem", "Depedency"]


class Depedency(BaseModel):
    node_id: str = FieldInfo(alias="nodeId")

    type: str


class NodeItem(BaseModel):
    call_id: Optional[str] = FieldInfo(alias="callId", default=None)

    depedency: Optional[Depedency] = None
    """请求/响应中的节点依赖变量类"""

    description: Optional[str] = None

    editable: Optional[bool] = None

    enable: Optional[bool] = None

    name: Optional[str] = None

    node_id: Optional[str] = FieldInfo(alias="nodeId", default=None)

    parameters: Optional[object] = None

    position: Optional[PositionItem] = None
    """请求/响应中的前端相对位置变量类"""

    service_id: Optional[str] = FieldInfo(alias="serviceId", default=None)

    step_id: Optional[str] = FieldInfo(alias="stepId", default=None)
