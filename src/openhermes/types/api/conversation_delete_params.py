# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ConversationDeleteParams"]


class ConversationDeleteParams(TypedDict, total=False):
    conversation_list: Required[Annotated[List[str], PropertyInfo(alias="conversationList")]]
