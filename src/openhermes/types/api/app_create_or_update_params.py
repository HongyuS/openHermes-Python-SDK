# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .app_type import AppType
from .app_link_param import AppLinkParam
from .app_flow_info_param import AppFlowInfoParam
from .app_permission_data_param import AppPermissionDataParam

__all__ = ["AppCreateOrUpdateParams"]


class AppCreateOrUpdateParams(TypedDict, total=False):
    app_type: Required[Annotated[AppType, PropertyInfo(alias="appType")]]
    """应用类型"""

    description: Required[str]
    """应用简介"""

    name: Required[str]
    """应用名称"""

    app_id: Annotated[Optional[str], PropertyInfo(alias="appId")]
    """应用 ID"""

    dialog_rounds: Annotated[int, PropertyInfo(alias="dialogRounds")]
    """对话轮次（1 ～ 10）"""

    icon: str
    """图标"""

    links: Iterable[AppLinkParam]
    """相关链接"""

    mcp_service: Annotated[List[str], PropertyInfo(alias="mcpService")]
    """MCP 服务 id 列表"""

    permission: AppPermissionDataParam
    """权限配置"""

    recommended_questions: Annotated[List[str], PropertyInfo(alias="recommendedQuestions")]
    """推荐问题"""

    workflows: Iterable[AppFlowInfoParam]
    """工作流信息列表"""
