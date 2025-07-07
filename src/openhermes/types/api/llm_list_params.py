# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["LlmListParams"]


class LlmListParams(TypedDict, total=False):
    llm_id: Annotated[Optional[str], PropertyInfo(alias="llmId")]
    """大模型 ID"""
