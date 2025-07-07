# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["KnowledgeListResponse", "Result", "ResultTeamKBList", "ResultTeamKBListKBList"]


class ResultTeamKBListKBList(BaseModel):
    description: str
    """知识库描述"""

    is_used: bool = FieldInfo(alias="isUsed")
    """是否使用"""

    kb_id: str = FieldInfo(alias="kbId")
    """知识库 ID"""

    kb_name: str = FieldInfo(alias="kbName")
    """知识库名称"""


class ResultTeamKBList(BaseModel):
    team_id: str = FieldInfo(alias="teamId")
    """团队 ID"""

    team_name: str = FieldInfo(alias="teamName")
    """团队名称"""

    kb_list: Optional[List[ResultTeamKBListKBList]] = None
    """知识库列表"""


class Result(BaseModel):
    team_kb_list: Optional[List[ResultTeamKBList]] = FieldInfo(alias="teamKbList", default=None)
    """团队知识库列表"""


class KnowledgeListResponse(BaseModel):
    code: int

    message: str

    result: Result
    """GET /api/knowledge Result 数据结构"""
