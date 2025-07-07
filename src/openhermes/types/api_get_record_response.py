# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .comment_type import CommentType

__all__ = [
    "APIGetRecordResponse",
    "Result",
    "ResultRecord",
    "ResultRecordContent",
    "ResultRecordMetadata",
    "ResultRecordDocument",
    "ResultRecordFlow",
    "ResultRecordFlowStep",
]


class ResultRecordContent(BaseModel):
    answer: str

    question: str

    data: Optional[object] = None

    facts: Optional[List[str]] = None
    """[运行后修改]与 Record 关联的事实信息"""


class ResultRecordMetadata(BaseModel):
    feature: Optional[object] = None

    input_tokens: Optional[int] = FieldInfo(alias="inputTokens", default=None)

    output_tokens: Optional[int] = FieldInfo(alias="outputTokens", default=None)

    time_cost: Optional[float] = FieldInfo(alias="timeCost", default=None)


class ResultRecordDocument(BaseModel):
    associated: Literal["question", "answer"]

    conversation_id: str

    name: str

    size: float

    type: str

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    created_at: Optional[float] = None

    user_sub: None = None


class ResultRecordFlowStep(BaseModel):
    input: object

    output: object

    step_id: str = FieldInfo(alias="stepId")

    step_status: Literal["running", "success", "error", "param"] = FieldInfo(alias="stepStatus")
    """步骤状态"""


class ResultRecordFlow(BaseModel):
    id: str

    flow_id: str = FieldInfo(alias="flowId")

    record_id: str = FieldInfo(alias="recordId")

    step_num: int = FieldInfo(alias="stepNum")

    steps: List[ResultRecordFlowStep]


class ResultRecord(BaseModel):
    id: str

    content: ResultRecordContent
    """Record 表子项：Record 加密前的数据结构"""

    conversation_id: str = FieldInfo(alias="conversationId")

    created_at: float = FieldInfo(alias="createdAt")

    group_id: str = FieldInfo(alias="groupId")

    metadata: ResultRecordMetadata
    """Record 表子项：Record 的元信息"""

    task_id: str = FieldInfo(alias="taskId")

    comment: Optional[CommentType] = None
    """点赞点踩类型"""

    document: Optional[List[ResultRecordDocument]] = None

    flow: Optional[ResultRecordFlow] = None
    """Flow 的执行信息"""


class Result(BaseModel):
    records: List[ResultRecord]


class APIGetRecordResponse(BaseModel):
    code: int

    message: str

    result: Result
    """GET /api/record/{conversation_id} Result 数据结构"""
