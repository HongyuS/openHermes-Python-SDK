# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Optional, cast
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.api import (
    McpType,
    mcp_get_list_params,
    mcp_get_detail_params,
    mcp_create_or_update_params,
    mcp_activate_or_deactivate_params,
)
from ..._base_client import make_request_options
from ...types.api.mcp_type import McpType
from ...types.api.mcp_delete_response import McpDeleteResponse
from ...types.api.mcp_get_list_response import McpGetListResponse
from ...types.api.mcp_get_detail_response import McpGetDetailResponse
from ...types.api.mcp_create_or_update_response import McpCreateOrUpdateResponse
from ...types.api.mcp_activate_or_deactivate_response import McpActivateOrDeactivateResponse

__all__ = ["McpResource", "AsyncMcpResource"]


class McpResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> McpResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/openhermes-python#accessing-raw-response-data-eg-headers
        """
        return McpResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> McpResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/openhermes-python#with_streaming_response
        """
        return McpResourceWithStreamingResponse(self)

    def delete(
        self,
        service_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> McpDeleteResponse:
        """
        删除服务

        Args:
          service_id: 服务 ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not service_id:
            raise ValueError(f"Expected a non-empty value for `service_id` but received {service_id!r}")
        return self._delete(
            f"/api/mcp/{service_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpDeleteResponse,
        )

    def activate_or_deactivate(
        self,
        service_id: str,
        *,
        active: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> McpActivateOrDeactivateResponse:
        """
        激活/取消激活 mcp

        Args:
          service_id: 服务 ID

          active: 是否激活 mcp 服务

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not service_id:
            raise ValueError(f"Expected a non-empty value for `service_id` but received {service_id!r}")
        return self._post(
            f"/api/mcp/{service_id}",
            body=maybe_transform({"active": active}, mcp_activate_or_deactivate_params.McpActivateOrDeactivateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpActivateOrDeactivateResponse,
        )

    def create_or_update(
        self,
        *,
        config: str,
        description: str,
        name: str,
        icon: str | NotGiven = NOT_GIVEN,
        mcp_type: McpType | NotGiven = NOT_GIVEN,
        service_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> McpCreateOrUpdateResponse:
        """
        新建或更新 MCP 服务

        Args:
          config: MCP 服务配置

          description: MCP 服务描述

          name: MCP 服务名称

          icon: 图标

          mcp_type: MCP 传输协议(Stdio/SSE/Streamable)

          service_id: 服务 ID（更新时传递）

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/mcp",
            body=maybe_transform(
                {
                    "config": config,
                    "description": description,
                    "name": name,
                    "icon": icon,
                    "mcp_type": mcp_type,
                    "service_id": service_id,
                },
                mcp_create_or_update_params.McpCreateOrUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpCreateOrUpdateResponse,
        )

    def get_detail(
        self,
        service_id: str,
        *,
        edit: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> McpGetDetailResponse:
        """
        获取 MCP 服务详情

        Args:
          service_id: 服务 ID

          edit: 是否为编辑模式

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not service_id:
            raise ValueError(f"Expected a non-empty value for `service_id` but received {service_id!r}")
        return self._get(
            f"/api/mcp/{service_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"edit": edit}, mcp_get_detail_params.McpGetDetailParams),
            ),
            cast_to=McpGetDetailResponse,
        )

    def get_list(
        self,
        *,
        is_active: Optional[bool] | NotGiven = NOT_GIVEN,
        keyword: Optional[str] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        search_type: Literal["all", "name", "author"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> McpGetListResponse:
        """
        获取服务列表

        Args:
          is_active: 是否激活

          keyword: 搜索关键字

          page: 页码

          page_size: 每页数量

          search_type: 搜索类型

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            McpGetListResponse,
            self._get(
                "/api/mcp",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "is_active": is_active,
                            "keyword": keyword,
                            "page": page,
                            "page_size": page_size,
                            "search_type": search_type,
                        },
                        mcp_get_list_params.McpGetListParams,
                    ),
                ),
                cast_to=cast(
                    Any, McpGetListResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncMcpResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMcpResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/openhermes-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMcpResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMcpResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/openhermes-python#with_streaming_response
        """
        return AsyncMcpResourceWithStreamingResponse(self)

    async def delete(
        self,
        service_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> McpDeleteResponse:
        """
        删除服务

        Args:
          service_id: 服务 ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not service_id:
            raise ValueError(f"Expected a non-empty value for `service_id` but received {service_id!r}")
        return await self._delete(
            f"/api/mcp/{service_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpDeleteResponse,
        )

    async def activate_or_deactivate(
        self,
        service_id: str,
        *,
        active: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> McpActivateOrDeactivateResponse:
        """
        激活/取消激活 mcp

        Args:
          service_id: 服务 ID

          active: 是否激活 mcp 服务

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not service_id:
            raise ValueError(f"Expected a non-empty value for `service_id` but received {service_id!r}")
        return await self._post(
            f"/api/mcp/{service_id}",
            body=await async_maybe_transform(
                {"active": active}, mcp_activate_or_deactivate_params.McpActivateOrDeactivateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpActivateOrDeactivateResponse,
        )

    async def create_or_update(
        self,
        *,
        config: str,
        description: str,
        name: str,
        icon: str | NotGiven = NOT_GIVEN,
        mcp_type: McpType | NotGiven = NOT_GIVEN,
        service_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> McpCreateOrUpdateResponse:
        """
        新建或更新 MCP 服务

        Args:
          config: MCP 服务配置

          description: MCP 服务描述

          name: MCP 服务名称

          icon: 图标

          mcp_type: MCP 传输协议(Stdio/SSE/Streamable)

          service_id: 服务 ID（更新时传递）

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/mcp",
            body=await async_maybe_transform(
                {
                    "config": config,
                    "description": description,
                    "name": name,
                    "icon": icon,
                    "mcp_type": mcp_type,
                    "service_id": service_id,
                },
                mcp_create_or_update_params.McpCreateOrUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpCreateOrUpdateResponse,
        )

    async def get_detail(
        self,
        service_id: str,
        *,
        edit: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> McpGetDetailResponse:
        """
        获取 MCP 服务详情

        Args:
          service_id: 服务 ID

          edit: 是否为编辑模式

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not service_id:
            raise ValueError(f"Expected a non-empty value for `service_id` but received {service_id!r}")
        return await self._get(
            f"/api/mcp/{service_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"edit": edit}, mcp_get_detail_params.McpGetDetailParams),
            ),
            cast_to=McpGetDetailResponse,
        )

    async def get_list(
        self,
        *,
        is_active: Optional[bool] | NotGiven = NOT_GIVEN,
        keyword: Optional[str] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        search_type: Literal["all", "name", "author"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> McpGetListResponse:
        """
        获取服务列表

        Args:
          is_active: 是否激活

          keyword: 搜索关键字

          page: 页码

          page_size: 每页数量

          search_type: 搜索类型

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            McpGetListResponse,
            await self._get(
                "/api/mcp",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {
                            "is_active": is_active,
                            "keyword": keyword,
                            "page": page,
                            "page_size": page_size,
                            "search_type": search_type,
                        },
                        mcp_get_list_params.McpGetListParams,
                    ),
                ),
                cast_to=cast(
                    Any, McpGetListResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class McpResourceWithRawResponse:
    def __init__(self, mcp: McpResource) -> None:
        self._mcp = mcp

        self.delete = to_raw_response_wrapper(
            mcp.delete,
        )
        self.activate_or_deactivate = to_raw_response_wrapper(
            mcp.activate_or_deactivate,
        )
        self.create_or_update = to_raw_response_wrapper(
            mcp.create_or_update,
        )
        self.get_detail = to_raw_response_wrapper(
            mcp.get_detail,
        )
        self.get_list = to_raw_response_wrapper(
            mcp.get_list,
        )


class AsyncMcpResourceWithRawResponse:
    def __init__(self, mcp: AsyncMcpResource) -> None:
        self._mcp = mcp

        self.delete = async_to_raw_response_wrapper(
            mcp.delete,
        )
        self.activate_or_deactivate = async_to_raw_response_wrapper(
            mcp.activate_or_deactivate,
        )
        self.create_or_update = async_to_raw_response_wrapper(
            mcp.create_or_update,
        )
        self.get_detail = async_to_raw_response_wrapper(
            mcp.get_detail,
        )
        self.get_list = async_to_raw_response_wrapper(
            mcp.get_list,
        )


class McpResourceWithStreamingResponse:
    def __init__(self, mcp: McpResource) -> None:
        self._mcp = mcp

        self.delete = to_streamed_response_wrapper(
            mcp.delete,
        )
        self.activate_or_deactivate = to_streamed_response_wrapper(
            mcp.activate_or_deactivate,
        )
        self.create_or_update = to_streamed_response_wrapper(
            mcp.create_or_update,
        )
        self.get_detail = to_streamed_response_wrapper(
            mcp.get_detail,
        )
        self.get_list = to_streamed_response_wrapper(
            mcp.get_list,
        )


class AsyncMcpResourceWithStreamingResponse:
    def __init__(self, mcp: AsyncMcpResource) -> None:
        self._mcp = mcp

        self.delete = async_to_streamed_response_wrapper(
            mcp.delete,
        )
        self.activate_or_deactivate = async_to_streamed_response_wrapper(
            mcp.activate_or_deactivate,
        )
        self.create_or_update = async_to_streamed_response_wrapper(
            mcp.create_or_update,
        )
        self.get_detail = async_to_streamed_response_wrapper(
            mcp.get_detail,
        )
        self.get_list = async_to_streamed_response_wrapper(
            mcp.get_list,
        )
