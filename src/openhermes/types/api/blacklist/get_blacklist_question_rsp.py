# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["GetBlacklistQuestionRsp", "Result", "ResultQuestionList"]


class ResultQuestionList(BaseModel):
    answer: str

    question: str

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    is_audited: Optional[bool] = None

    reason: Optional[str] = None

    reason_type: Optional[str] = None

    updated_at: Optional[float] = None


class Result(BaseModel):
    question_list: List[ResultQuestionList]


class GetBlacklistQuestionRsp(BaseModel):
    code: int

    message: str

    result: Result
    """GET /api/blacklist/question Result 数据结构"""
