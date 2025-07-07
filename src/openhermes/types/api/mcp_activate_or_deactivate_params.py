# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["McpActivateOrDeactivateParams"]


class McpActivateOrDeactivateParams(TypedDict, total=False):
    active: Required[bool]
    """是否激活 mcp 服务"""
