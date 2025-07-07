# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .edge_item_param import EdgeItemParam
from .node_item_param import NodeItemParam
from .position_item_param import PositionItemParam

__all__ = ["FlowUpdateParams", "Flow"]


class FlowUpdateParams(TypedDict, total=False):
    app_id: Required[Annotated[str, PropertyInfo(alias="appId")]]

    flow_id: Required[Annotated[str, PropertyInfo(alias="flowId")]]

    flow: Required[Flow]
    """请求/响应中的流变量类"""


class Flow(TypedDict, total=False):
    connectivity: bool
    """图的开始节点和结束节点是否联通，并且除结束节点都有出边"""

    created_at: Annotated[Optional[float], PropertyInfo(alias="createdAt")]

    debug: bool

    description: str

    edges: Iterable[EdgeItemParam]

    editable: bool

    enable: bool

    flow_id: Annotated[Optional[str], PropertyInfo(alias="flowId")]

    focus_point: Annotated[PositionItemParam, PropertyInfo(alias="focusPoint")]
    """请求/响应中的前端相对位置变量类"""

    name: str

    nodes: Iterable[NodeItemParam]
