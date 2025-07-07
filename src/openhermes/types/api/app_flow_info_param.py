# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AppFlowInfoParam"]


class AppFlowInfoParam(TypedDict, total=False):
    id: Required[str]
    """工作流 ID"""

    debug: Required[bool]
    """是否经过调试"""

    description: Required[str]
    """工作流简介"""

    name: Required[str]
    """工作流名称"""
