# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .position_item_param import PositionItemParam

__all__ = ["NodeItemParam", "Depedency"]


class Depedency(TypedDict, total=False):
    node_id: Required[Annotated[str, PropertyInfo(alias="nodeId")]]

    type: Required[str]


class NodeItemParam(TypedDict, total=False):
    call_id: Annotated[str, PropertyInfo(alias="callId")]

    depedency: Optional[Depedency]
    """请求/响应中的节点依赖变量类"""

    description: str

    editable: bool

    enable: bool

    name: str

    node_id: Annotated[str, PropertyInfo(alias="nodeId")]

    parameters: object

    position: PositionItemParam
    """请求/响应中的前端相对位置变量类"""

    service_id: Annotated[str, PropertyInfo(alias="serviceId")]

    step_id: Annotated[str, PropertyInfo(alias="stepId")]
