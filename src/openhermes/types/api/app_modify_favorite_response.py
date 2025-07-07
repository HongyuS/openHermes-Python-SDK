# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .response_data import ResponseData

__all__ = ["AppModifyFavoriteResponse", "ModFavAppRsp", "ModFavAppRspResult"]


class ModFavAppRspResult(BaseModel):
    app_id: str = FieldInfo(alias="appId")
    """应用 ID"""

    favorited: bool
    """是否已收藏"""


class ModFavAppRsp(BaseModel):
    code: int

    message: str

    result: ModFavAppRspResult
    """PUT /api/app/{appId} Result 数据结构"""


AppModifyFavoriteResponse: TypeAlias = Union[ModFavAppRsp, ResponseData]
