# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .response_data import ResponseData

__all__ = [
    "AppListRecentResponse",
    "GetRecentAppListRsp",
    "GetRecentAppListRspResult",
    "GetRecentAppListRspResultApplication",
]


class GetRecentAppListRspResultApplication(BaseModel):
    app_id: str = FieldInfo(alias="appId")
    """应用 ID"""

    name: str
    """应用名称"""


class GetRecentAppListRspResult(BaseModel):
    applications: List[GetRecentAppListRspResultApplication]
    """最近使用的应用列表"""


class GetRecentAppListRsp(BaseModel):
    code: int

    message: str

    result: GetRecentAppListRspResult
    """GET /api/app/recent Result 数据结构"""


AppListRecentResponse: TypeAlias = Union[GetRecentAppListRsp, ResponseData]
