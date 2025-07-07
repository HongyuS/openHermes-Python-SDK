# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .app_link import AppLink
from .app_type import AppType
from ..._models import BaseModel
from .app_flow_info import AppFlowInfo
from .response_data import ResponseData
from .app_permission_data import AppPermissionData

__all__ = ["AppRetrieveResponse", "GetAppPropertyRsp", "GetAppPropertyRspResult"]


class GetAppPropertyRspResult(BaseModel):
    app_id: str = FieldInfo(alias="appId")
    """应用 ID"""

    app_type: AppType = FieldInfo(alias="appType")
    """应用类型"""

    description: str
    """应用简介"""

    name: str
    """应用名称"""

    published: bool
    """是否已发布"""

    dialog_rounds: Optional[int] = FieldInfo(alias="dialogRounds", default=None)
    """对话轮次（1 ～ 10）"""

    icon: Optional[str] = None
    """图标"""

    links: Optional[List[AppLink]] = None
    """相关链接"""

    mcp_service: Optional[List[str]] = FieldInfo(alias="mcpService", default=None)
    """MCP 服务 id 列表"""

    permission: Optional[AppPermissionData] = None
    """权限配置"""

    recommended_questions: Optional[List[str]] = FieldInfo(alias="recommendedQuestions", default=None)
    """推荐问题"""

    workflows: Optional[List[AppFlowInfo]] = None
    """工作流信息列表"""


class GetAppPropertyRsp(BaseModel):
    code: int

    message: str

    result: GetAppPropertyRspResult
    """GET /api/app/{appId} Result 数据结构"""


AppRetrieveResponse: TypeAlias = Union[GetAppPropertyRsp, ResponseData]
