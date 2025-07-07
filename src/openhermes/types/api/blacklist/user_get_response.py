# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel

__all__ = ["UserGetResponse", "Result"]


class Result(BaseModel):
    user_subs: List[str]


class UserGetResponse(BaseModel):
    code: int

    message: str

    result: Result
    """GET /api/blacklist/user Result 数据结构"""
