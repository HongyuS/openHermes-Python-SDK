# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ConversationCreateParams"]


class ConversationCreateParams(TypedDict, total=False):
    app_id: Annotated[str, PropertyInfo(alias="appId")]

    debug: bool

    kb_ids: List[str]

    llm_id: str
