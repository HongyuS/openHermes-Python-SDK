# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .edge_item import EdgeItem
from .node_item import NodeItem
from .position_item import PositionItem

__all__ = ["FlowItemOutput"]


class FlowItemOutput(BaseModel):
    connectivity: Optional[bool] = None
    """图的开始节点和结束节点是否联通，并且除结束节点都有出边"""

    created_at: Optional[float] = FieldInfo(alias="createdAt", default=None)

    debug: Optional[bool] = None

    description: Optional[str] = None

    edges: Optional[List[EdgeItem]] = None

    editable: Optional[bool] = None

    enable: Optional[bool] = None

    flow_id: Optional[str] = FieldInfo(alias="flowId", default=None)

    focus_point: Optional[PositionItem] = FieldInfo(alias="focusPoint", default=None)
    """请求/响应中的前端相对位置变量类"""

    name: Optional[str] = None

    nodes: Optional[List[NodeItem]] = None
