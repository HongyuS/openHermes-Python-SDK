# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["QuestionChangeParams"]


class QuestionChangeParams(TypedDict, total=False):
    id: Required[str]

    answer: Required[str]

    is_deletion: Required[int]

    question: Required[str]
