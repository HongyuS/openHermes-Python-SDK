# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.api import flow_get_params, flow_delete_params, flow_update_params
from ..._base_client import make_request_options
from ...types.api.flow_get_response import FlowGetResponse
from ...types.api.flow_delete_response import FlowDeleteResponse
from ...types.api.flow_update_response import FlowUpdateResponse
from ...types.api.flow_get_services_response import FlowGetServicesResponse

__all__ = ["FlowResource", "AsyncFlowResource"]


class FlowResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FlowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HongyuS/openHermes-Python-SDK#accessing-raw-response-data-eg-headers
        """
        return FlowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FlowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HongyuS/openHermes-Python-SDK#with_streaming_response
        """
        return FlowResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        app_id: str,
        flow_id: str,
        flow: flow_update_params.Flow,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FlowUpdateResponse:
        """
        修改流拓扑结构

        Args:
          flow: 请求/响应中的流变量类

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/api/flow",
            body=maybe_transform({"flow": flow}, flow_update_params.FlowUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "app_id": app_id,
                        "flow_id": flow_id,
                    },
                    flow_update_params.FlowUpdateParams,
                ),
            ),
            cast_to=FlowUpdateResponse,
        )

    def delete(
        self,
        *,
        app_id: str,
        flow_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FlowDeleteResponse:
        """
        删除流拓扑结构

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/api/flow",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "app_id": app_id,
                        "flow_id": flow_id,
                    },
                    flow_delete_params.FlowDeleteParams,
                ),
            ),
            cast_to=FlowDeleteResponse,
        )

    def get(
        self,
        *,
        app_id: str,
        flow_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FlowGetResponse:
        """
        获取流拓扑结构

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/flow",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "app_id": app_id,
                        "flow_id": flow_id,
                    },
                    flow_get_params.FlowGetParams,
                ),
            ),
            cast_to=FlowGetResponse,
        )

    def get_services(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FlowGetServicesResponse:
        """获取用户可访问的节点元数据所在服务的信息"""
        return self._get(
            "/api/flow/service",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FlowGetServicesResponse,
        )


class AsyncFlowResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFlowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HongyuS/openHermes-Python-SDK#accessing-raw-response-data-eg-headers
        """
        return AsyncFlowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFlowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HongyuS/openHermes-Python-SDK#with_streaming_response
        """
        return AsyncFlowResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        app_id: str,
        flow_id: str,
        flow: flow_update_params.Flow,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FlowUpdateResponse:
        """
        修改流拓扑结构

        Args:
          flow: 请求/响应中的流变量类

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/api/flow",
            body=await async_maybe_transform({"flow": flow}, flow_update_params.FlowUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "app_id": app_id,
                        "flow_id": flow_id,
                    },
                    flow_update_params.FlowUpdateParams,
                ),
            ),
            cast_to=FlowUpdateResponse,
        )

    async def delete(
        self,
        *,
        app_id: str,
        flow_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FlowDeleteResponse:
        """
        删除流拓扑结构

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/api/flow",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "app_id": app_id,
                        "flow_id": flow_id,
                    },
                    flow_delete_params.FlowDeleteParams,
                ),
            ),
            cast_to=FlowDeleteResponse,
        )

    async def get(
        self,
        *,
        app_id: str,
        flow_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FlowGetResponse:
        """
        获取流拓扑结构

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/flow",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "app_id": app_id,
                        "flow_id": flow_id,
                    },
                    flow_get_params.FlowGetParams,
                ),
            ),
            cast_to=FlowGetResponse,
        )

    async def get_services(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FlowGetServicesResponse:
        """获取用户可访问的节点元数据所在服务的信息"""
        return await self._get(
            "/api/flow/service",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FlowGetServicesResponse,
        )


class FlowResourceWithRawResponse:
    def __init__(self, flow: FlowResource) -> None:
        self._flow = flow

        self.update = to_raw_response_wrapper(
            flow.update,
        )
        self.delete = to_raw_response_wrapper(
            flow.delete,
        )
        self.get = to_raw_response_wrapper(
            flow.get,
        )
        self.get_services = to_raw_response_wrapper(
            flow.get_services,
        )


class AsyncFlowResourceWithRawResponse:
    def __init__(self, flow: AsyncFlowResource) -> None:
        self._flow = flow

        self.update = async_to_raw_response_wrapper(
            flow.update,
        )
        self.delete = async_to_raw_response_wrapper(
            flow.delete,
        )
        self.get = async_to_raw_response_wrapper(
            flow.get,
        )
        self.get_services = async_to_raw_response_wrapper(
            flow.get_services,
        )


class FlowResourceWithStreamingResponse:
    def __init__(self, flow: FlowResource) -> None:
        self._flow = flow

        self.update = to_streamed_response_wrapper(
            flow.update,
        )
        self.delete = to_streamed_response_wrapper(
            flow.delete,
        )
        self.get = to_streamed_response_wrapper(
            flow.get,
        )
        self.get_services = to_streamed_response_wrapper(
            flow.get_services,
        )


class AsyncFlowResourceWithStreamingResponse:
    def __init__(self, flow: AsyncFlowResource) -> None:
        self._flow = flow

        self.update = async_to_streamed_response_wrapper(
            flow.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            flow.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            flow.get,
        )
        self.get_services = async_to_streamed_response_wrapper(
            flow.get_services,
        )
