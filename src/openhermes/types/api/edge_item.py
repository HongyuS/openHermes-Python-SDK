# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["EdgeItem"]


class EdgeItem(BaseModel):
    branch_id: str = FieldInfo(alias="branchId")

    edge_id: str = FieldInfo(alias="edgeId")

    source_node: str = FieldInfo(alias="sourceNode")

    target_node: str = FieldInfo(alias="targetNode")

    type: Optional[str] = None
