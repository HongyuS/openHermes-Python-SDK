# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .app_type import AppType
from ..._models import BaseModel
from .response_data import ResponseData

__all__ = ["AppListResponse", "GetAppListRsp", "GetAppListRspResult", "GetAppListRspResultApplication"]


class GetAppListRspResultApplication(BaseModel):
    app_id: str = FieldInfo(alias="appId")
    """应用 ID"""

    app_type: AppType = FieldInfo(alias="appType")
    """应用类型"""

    author: str
    """应用作者"""

    description: str
    """应用简介"""

    favorited: bool
    """是否已收藏"""

    icon: str
    """应用图标"""

    name: str
    """应用名称"""

    published: Optional[bool] = None
    """是否已发布"""


class GetAppListRspResult(BaseModel):
    applications: List[GetAppListRspResultApplication]
    """应用列表"""

    current_page: int = FieldInfo(alias="currentPage")
    """当前页码"""

    total_apps: int = FieldInfo(alias="totalApps")
    """总应用数"""


class GetAppListRsp(BaseModel):
    code: int

    message: str

    result: GetAppListRspResult
    """GET /api/app Result 数据结构"""


AppListResponse: TypeAlias = Union[GetAppListRsp, ResponseData]
