# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, Iterable, Optional, cast

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
    AppType,
    app_list_params,
    app_get_recent_params,
    app_modify_favorite_params,
    app_create_or_update_params,
)
from ..._base_client import make_request_options
from ...types.api.app_type import AppType
from ...types.api.app_link_param import AppLinkParam
from ...types.api.app_list_response import AppListResponse
from ...types.api.app_delete_response import AppDeleteResponse
from ...types.api.app_flow_info_param import AppFlowInfoParam
from ...types.api.app_retrieve_response import AppRetrieveResponse
from ...types.api.base_app_operation_rsp import BaseAppOperationRsp
from ...types.api.app_get_recent_response import AppGetRecentResponse
from ...types.api.app_permission_data_param import AppPermissionDataParam
from ...types.api.app_modify_favorite_response import AppModifyFavoriteResponse
from ...types.api.app_create_or_update_response import AppCreateOrUpdateResponse

__all__ = ["AppResource", "AsyncAppResource"]


class AppResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AppResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HongyuS/openHermes-Python-SDK#accessing-raw-response-data-eg-headers
        """
        return AppResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AppResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HongyuS/openHermes-Python-SDK#with_streaming_response
        """
        return AppResourceWithStreamingResponse(self)

    def retrieve(
        self,
        app_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppRetrieveResponse:
        """
        获取应用详情

        Args:
          app_id: 应用 ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return cast(
            AppRetrieveResponse,
            self._get(
                f"/api/app/{app_id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, AppRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        app_type: Optional[AppType] | NotGiven = NOT_GIVEN,
        created_by_me: bool | NotGiven = NOT_GIVEN,
        favorited: bool | NotGiven = NOT_GIVEN,
        keyword: Optional[str] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppListResponse:
        """
        获取应用列表

        Args:
          app_type: 应用类型

          created_by_me: 筛选我创建的

          favorited: 筛选我收藏的

          keyword: 搜索关键字

          page: 页码

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            AppListResponse,
            self._get(
                "/api/app",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "app_type": app_type,
                            "created_by_me": created_by_me,
                            "favorited": favorited,
                            "keyword": keyword,
                            "page": page,
                        },
                        app_list_params.AppListParams,
                    ),
                ),
                cast_to=cast(Any, AppListResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def delete(
        self,
        app_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppDeleteResponse:
        """
        删除应用

        Args:
          app_id: 应用 ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return cast(
            AppDeleteResponse,
            self._delete(
                f"/api/app/{app_id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, AppDeleteResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def create_or_update(
        self,
        *,
        app_type: AppType,
        description: str,
        name: str,
        app_id: Optional[str] | NotGiven = NOT_GIVEN,
        dialog_rounds: int | NotGiven = NOT_GIVEN,
        icon: str | NotGiven = NOT_GIVEN,
        links: Iterable[AppLinkParam] | NotGiven = NOT_GIVEN,
        mcp_service: List[str] | NotGiven = NOT_GIVEN,
        permission: AppPermissionDataParam | NotGiven = NOT_GIVEN,
        recommended_questions: List[str] | NotGiven = NOT_GIVEN,
        workflows: Iterable[AppFlowInfoParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppCreateOrUpdateResponse:
        """
        创建或更新应用

        Args:
          app_type: 应用类型

          description: 应用简介

          name: 应用名称

          app_id: 应用 ID

          dialog_rounds: 对话轮次（1 ～ 10）

          icon: 图标

          links: 相关链接

          mcp_service: MCP 服务 id 列表

          permission: 权限配置

          recommended_questions: 推荐问题

          workflows: 工作流信息列表

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            AppCreateOrUpdateResponse,
            self._post(
                "/api/app",
                body=maybe_transform(
                    {
                        "app_type": app_type,
                        "description": description,
                        "name": name,
                        "app_id": app_id,
                        "dialog_rounds": dialog_rounds,
                        "icon": icon,
                        "links": links,
                        "mcp_service": mcp_service,
                        "permission": permission,
                        "recommended_questions": recommended_questions,
                        "workflows": workflows,
                    },
                    app_create_or_update_params.AppCreateOrUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, AppCreateOrUpdateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def get_recent(
        self,
        *,
        count: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppGetRecentResponse:
        """
        获取最近使用的应用

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            AppGetRecentResponse,
            self._get(
                "/api/app/recent",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform({"count": count}, app_get_recent_params.AppGetRecentParams),
                ),
                cast_to=cast(
                    Any, AppGetRecentResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def modify_favorite(
        self,
        app_id: str,
        *,
        favorited: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppModifyFavoriteResponse:
        """
        更改应用收藏状态

        Args:
          app_id: 应用 ID

          favorited: 是否收藏

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return cast(
            AppModifyFavoriteResponse,
            self._put(
                f"/api/app/{app_id}",
                body=maybe_transform({"favorited": favorited}, app_modify_favorite_params.AppModifyFavoriteParams),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, AppModifyFavoriteResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def publish(
        self,
        app_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BaseAppOperationRsp:
        """
        发布应用

        Args:
          app_id: 应用 ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return self._post(
            f"/api/app/{app_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BaseAppOperationRsp,
        )


class AsyncAppResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAppResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HongyuS/openHermes-Python-SDK#accessing-raw-response-data-eg-headers
        """
        return AsyncAppResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAppResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HongyuS/openHermes-Python-SDK#with_streaming_response
        """
        return AsyncAppResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        app_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppRetrieveResponse:
        """
        获取应用详情

        Args:
          app_id: 应用 ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return cast(
            AppRetrieveResponse,
            await self._get(
                f"/api/app/{app_id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, AppRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def list(
        self,
        *,
        app_type: Optional[AppType] | NotGiven = NOT_GIVEN,
        created_by_me: bool | NotGiven = NOT_GIVEN,
        favorited: bool | NotGiven = NOT_GIVEN,
        keyword: Optional[str] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppListResponse:
        """
        获取应用列表

        Args:
          app_type: 应用类型

          created_by_me: 筛选我创建的

          favorited: 筛选我收藏的

          keyword: 搜索关键字

          page: 页码

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            AppListResponse,
            await self._get(
                "/api/app",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {
                            "app_type": app_type,
                            "created_by_me": created_by_me,
                            "favorited": favorited,
                            "keyword": keyword,
                            "page": page,
                        },
                        app_list_params.AppListParams,
                    ),
                ),
                cast_to=cast(Any, AppListResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def delete(
        self,
        app_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppDeleteResponse:
        """
        删除应用

        Args:
          app_id: 应用 ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return cast(
            AppDeleteResponse,
            await self._delete(
                f"/api/app/{app_id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, AppDeleteResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def create_or_update(
        self,
        *,
        app_type: AppType,
        description: str,
        name: str,
        app_id: Optional[str] | NotGiven = NOT_GIVEN,
        dialog_rounds: int | NotGiven = NOT_GIVEN,
        icon: str | NotGiven = NOT_GIVEN,
        links: Iterable[AppLinkParam] | NotGiven = NOT_GIVEN,
        mcp_service: List[str] | NotGiven = NOT_GIVEN,
        permission: AppPermissionDataParam | NotGiven = NOT_GIVEN,
        recommended_questions: List[str] | NotGiven = NOT_GIVEN,
        workflows: Iterable[AppFlowInfoParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppCreateOrUpdateResponse:
        """
        创建或更新应用

        Args:
          app_type: 应用类型

          description: 应用简介

          name: 应用名称

          app_id: 应用 ID

          dialog_rounds: 对话轮次（1 ～ 10）

          icon: 图标

          links: 相关链接

          mcp_service: MCP 服务 id 列表

          permission: 权限配置

          recommended_questions: 推荐问题

          workflows: 工作流信息列表

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            AppCreateOrUpdateResponse,
            await self._post(
                "/api/app",
                body=await async_maybe_transform(
                    {
                        "app_type": app_type,
                        "description": description,
                        "name": name,
                        "app_id": app_id,
                        "dialog_rounds": dialog_rounds,
                        "icon": icon,
                        "links": links,
                        "mcp_service": mcp_service,
                        "permission": permission,
                        "recommended_questions": recommended_questions,
                        "workflows": workflows,
                    },
                    app_create_or_update_params.AppCreateOrUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, AppCreateOrUpdateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def get_recent(
        self,
        *,
        count: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppGetRecentResponse:
        """
        获取最近使用的应用

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            AppGetRecentResponse,
            await self._get(
                "/api/app/recent",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform({"count": count}, app_get_recent_params.AppGetRecentParams),
                ),
                cast_to=cast(
                    Any, AppGetRecentResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def modify_favorite(
        self,
        app_id: str,
        *,
        favorited: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppModifyFavoriteResponse:
        """
        更改应用收藏状态

        Args:
          app_id: 应用 ID

          favorited: 是否收藏

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return cast(
            AppModifyFavoriteResponse,
            await self._put(
                f"/api/app/{app_id}",
                body=await async_maybe_transform(
                    {"favorited": favorited}, app_modify_favorite_params.AppModifyFavoriteParams
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, AppModifyFavoriteResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def publish(
        self,
        app_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BaseAppOperationRsp:
        """
        发布应用

        Args:
          app_id: 应用 ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return await self._post(
            f"/api/app/{app_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BaseAppOperationRsp,
        )


class AppResourceWithRawResponse:
    def __init__(self, app: AppResource) -> None:
        self._app = app

        self.retrieve = to_raw_response_wrapper(
            app.retrieve,
        )
        self.list = to_raw_response_wrapper(
            app.list,
        )
        self.delete = to_raw_response_wrapper(
            app.delete,
        )
        self.create_or_update = to_raw_response_wrapper(
            app.create_or_update,
        )
        self.get_recent = to_raw_response_wrapper(
            app.get_recent,
        )
        self.modify_favorite = to_raw_response_wrapper(
            app.modify_favorite,
        )
        self.publish = to_raw_response_wrapper(
            app.publish,
        )


class AsyncAppResourceWithRawResponse:
    def __init__(self, app: AsyncAppResource) -> None:
        self._app = app

        self.retrieve = async_to_raw_response_wrapper(
            app.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            app.list,
        )
        self.delete = async_to_raw_response_wrapper(
            app.delete,
        )
        self.create_or_update = async_to_raw_response_wrapper(
            app.create_or_update,
        )
        self.get_recent = async_to_raw_response_wrapper(
            app.get_recent,
        )
        self.modify_favorite = async_to_raw_response_wrapper(
            app.modify_favorite,
        )
        self.publish = async_to_raw_response_wrapper(
            app.publish,
        )


class AppResourceWithStreamingResponse:
    def __init__(self, app: AppResource) -> None:
        self._app = app

        self.retrieve = to_streamed_response_wrapper(
            app.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            app.list,
        )
        self.delete = to_streamed_response_wrapper(
            app.delete,
        )
        self.create_or_update = to_streamed_response_wrapper(
            app.create_or_update,
        )
        self.get_recent = to_streamed_response_wrapper(
            app.get_recent,
        )
        self.modify_favorite = to_streamed_response_wrapper(
            app.modify_favorite,
        )
        self.publish = to_streamed_response_wrapper(
            app.publish,
        )


class AsyncAppResourceWithStreamingResponse:
    def __init__(self, app: AsyncAppResource) -> None:
        self._app = app

        self.retrieve = async_to_streamed_response_wrapper(
            app.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            app.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            app.delete,
        )
        self.create_or_update = async_to_streamed_response_wrapper(
            app.create_or_update,
        )
        self.get_recent = async_to_streamed_response_wrapper(
            app.get_recent,
        )
        self.modify_favorite = async_to_streamed_response_wrapper(
            app.modify_favorite,
        )
        self.publish = async_to_streamed_response_wrapper(
            app.publish,
        )
