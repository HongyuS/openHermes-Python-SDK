# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FlowGetParams"]


class FlowGetParams(TypedDict, total=False):
    app_id: Required[Annotated[str, PropertyInfo(alias="appId")]]

    flow_id: Required[Annotated[str, PropertyInfo(alias="flowId")]]
