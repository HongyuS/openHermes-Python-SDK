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
    service_list_params,
    service_update_params,
    service_retrieve_params,
    service_modify_favorite_params,
)
from ..._base_client import make_request_options
from ...types.api.service_list_response import ServiceListResponse
from ...types.api.service_delete_response import ServiceDeleteResponse
from ...types.api.service_update_response import ServiceUpdateResponse
from ...types.api.service_retrieve_response import ServiceRetrieveResponse
from ...types.api.service_modify_favorite_response import ServiceModifyFavoriteResponse

__all__ = ["ServiceResource", "AsyncServiceResource"]


class ServiceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ServiceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/openhermes-python#accessing-raw-response-data-eg-headers
        """
        return ServiceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ServiceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/openhermes-python#with_streaming_response
        """
        return ServiceResourceWithStreamingResponse(self)

    def retrieve(
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
    ) -> ServiceRetrieveResponse:
        """
        获取服务详情

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
            f"/api/service/{service_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"edit": edit}, service_retrieve_params.ServiceRetrieveParams),
            ),
            cast_to=ServiceRetrieveResponse,
        )

    def update(
        self,
        *,
        data: object,
        service_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceUpdateResponse:
        """
        上传并解析服务

        Args:
          data: 对应 YAML 内容的数据对象

          service_id: 服务 ID（更新时传递）

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/service",
            body=maybe_transform(
                {
                    "data": data,
                    "service_id": service_id,
                },
                service_update_params.ServiceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceUpdateResponse,
        )

    def list(
        self,
        *,
        created_by_me: bool | NotGiven = NOT_GIVEN,
        favorited: bool | NotGiven = NOT_GIVEN,
        keyword: Optional[str] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        search_type: Literal["all", "name", "description", "author"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceListResponse:
        """
        获取服务列表

        Args:
          created_by_me: 筛选我创建的

          favorited: 筛选我收藏的

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
            ServiceListResponse,
            self._get(
                "/api/service",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "created_by_me": created_by_me,
                            "favorited": favorited,
                            "keyword": keyword,
                            "page": page,
                            "page_size": page_size,
                            "search_type": search_type,
                        },
                        service_list_params.ServiceListParams,
                    ),
                ),
                cast_to=cast(
                    Any, ServiceListResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

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
    ) -> ServiceDeleteResponse:
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
            f"/api/service/{service_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceDeleteResponse,
        )

    def modify_favorite(
        self,
        service_id: str,
        *,
        favorited: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceModifyFavoriteResponse:
        """
        修改服务收藏状态

        Args:
          service_id: 服务 ID

          favorited: 是否收藏

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not service_id:
            raise ValueError(f"Expected a non-empty value for `service_id` but received {service_id!r}")
        return self._put(
            f"/api/service/{service_id}",
            body=maybe_transform({"favorited": favorited}, service_modify_favorite_params.ServiceModifyFavoriteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceModifyFavoriteResponse,
        )


class AsyncServiceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncServiceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/openhermes-python#accessing-raw-response-data-eg-headers
        """
        return AsyncServiceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncServiceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/openhermes-python#with_streaming_response
        """
        return AsyncServiceResourceWithStreamingResponse(self)

    async def retrieve(
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
    ) -> ServiceRetrieveResponse:
        """
        获取服务详情

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
            f"/api/service/{service_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"edit": edit}, service_retrieve_params.ServiceRetrieveParams),
            ),
            cast_to=ServiceRetrieveResponse,
        )

    async def update(
        self,
        *,
        data: object,
        service_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceUpdateResponse:
        """
        上传并解析服务

        Args:
          data: 对应 YAML 内容的数据对象

          service_id: 服务 ID（更新时传递）

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/service",
            body=await async_maybe_transform(
                {
                    "data": data,
                    "service_id": service_id,
                },
                service_update_params.ServiceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceUpdateResponse,
        )

    async def list(
        self,
        *,
        created_by_me: bool | NotGiven = NOT_GIVEN,
        favorited: bool | NotGiven = NOT_GIVEN,
        keyword: Optional[str] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        search_type: Literal["all", "name", "description", "author"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceListResponse:
        """
        获取服务列表

        Args:
          created_by_me: 筛选我创建的

          favorited: 筛选我收藏的

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
            ServiceListResponse,
            await self._get(
                "/api/service",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {
                            "created_by_me": created_by_me,
                            "favorited": favorited,
                            "keyword": keyword,
                            "page": page,
                            "page_size": page_size,
                            "search_type": search_type,
                        },
                        service_list_params.ServiceListParams,
                    ),
                ),
                cast_to=cast(
                    Any, ServiceListResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

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
    ) -> ServiceDeleteResponse:
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
            f"/api/service/{service_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceDeleteResponse,
        )

    async def modify_favorite(
        self,
        service_id: str,
        *,
        favorited: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceModifyFavoriteResponse:
        """
        修改服务收藏状态

        Args:
          service_id: 服务 ID

          favorited: 是否收藏

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not service_id:
            raise ValueError(f"Expected a non-empty value for `service_id` but received {service_id!r}")
        return await self._put(
            f"/api/service/{service_id}",
            body=await async_maybe_transform(
                {"favorited": favorited}, service_modify_favorite_params.ServiceModifyFavoriteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceModifyFavoriteResponse,
        )


class ServiceResourceWithRawResponse:
    def __init__(self, service: ServiceResource) -> None:
        self._service = service

        self.retrieve = to_raw_response_wrapper(
            service.retrieve,
        )
        self.update = to_raw_response_wrapper(
            service.update,
        )
        self.list = to_raw_response_wrapper(
            service.list,
        )
        self.delete = to_raw_response_wrapper(
            service.delete,
        )
        self.modify_favorite = to_raw_response_wrapper(
            service.modify_favorite,
        )


class AsyncServiceResourceWithRawResponse:
    def __init__(self, service: AsyncServiceResource) -> None:
        self._service = service

        self.retrieve = async_to_raw_response_wrapper(
            service.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            service.update,
        )
        self.list = async_to_raw_response_wrapper(
            service.list,
        )
        self.delete = async_to_raw_response_wrapper(
            service.delete,
        )
        self.modify_favorite = async_to_raw_response_wrapper(
            service.modify_favorite,
        )


class ServiceResourceWithStreamingResponse:
    def __init__(self, service: ServiceResource) -> None:
        self._service = service

        self.retrieve = to_streamed_response_wrapper(
            service.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            service.update,
        )
        self.list = to_streamed_response_wrapper(
            service.list,
        )
        self.delete = to_streamed_response_wrapper(
            service.delete,
        )
        self.modify_favorite = to_streamed_response_wrapper(
            service.modify_favorite,
        )


class AsyncServiceResourceWithStreamingResponse:
    def __init__(self, service: AsyncServiceResource) -> None:
        self._service = service

        self.retrieve = async_to_streamed_response_wrapper(
            service.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            service.update,
        )
        self.list = async_to_streamed_response_wrapper(
            service.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            service.delete,
        )
        self.modify_favorite = async_to_streamed_response_wrapper(
            service.modify_favorite,
        )
