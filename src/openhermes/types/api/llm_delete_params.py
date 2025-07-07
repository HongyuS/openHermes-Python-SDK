# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["LlmDeleteParams"]


class LlmDeleteParams(TypedDict, total=False):
    llm_id: Required[Annotated[str, PropertyInfo(alias="llmId")]]
    """大模型 ID"""
