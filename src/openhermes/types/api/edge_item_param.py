# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EdgeItemParam"]


class EdgeItemParam(TypedDict, total=False):
    branch_id: Required[Annotated[str, PropertyInfo(alias="branchId")]]

    edge_id: Required[Annotated[str, PropertyInfo(alias="edgeId")]]

    source_node: Required[Annotated[str, PropertyInfo(alias="sourceNode")]]

    target_node: Required[Annotated[str, PropertyInfo(alias="targetNode")]]

    type: str
