# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["APIChatParams", "App"]


class APIChatParams(TypedDict, total=False):
    question: Required[str]
    """用户输入"""

    app: Optional[App]
    """应用"""

    conversation_id: Annotated[str, PropertyInfo(alias="conversationId")]
    """聊天 ID"""

    debug: bool
    """是否调试"""

    files: List[str]
    """文件列表"""

    group_id: Annotated[Optional[str], PropertyInfo(alias="groupId")]
    """问答组 ID"""

    language: str
    """语言"""


class App(TypedDict, total=False):
    app_id: Required[Annotated[str, PropertyInfo(alias="appId")]]
    """应用 ID"""

    flow_id: Required[Annotated[str, PropertyInfo(alias="flowId")]]
    """Flow ID"""

    params: Required[object]
    """插件参数"""
