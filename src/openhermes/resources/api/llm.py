# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

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
from ...types.api import llm_list_params, llm_delete_params, llm_update_conv_params, llm_create_or_update_params
from ..._base_client import make_request_options
from ...types.api.llm_list_response import LlmListResponse
from ...types.api.llm_list_providers_response import LlmListProvidersResponse

__all__ = ["LlmResource", "AsyncLlmResource"]


class LlmResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LlmResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/openhermes-python#accessing-raw-response-data-eg-headers
        """
        return LlmResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LlmResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/openhermes-python#with_streaming_response
        """
        return LlmResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        llm_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LlmListResponse:
        """
        获取大模型列表

        Args:
          llm_id: 大模型 ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/llm",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"llm_id": llm_id}, llm_list_params.LlmListParams),
            ),
            cast_to=LlmListResponse,
        )

    def delete(
        self,
        *,
        llm_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        删除大模型配置

        Args:
          llm_id: 大模型 ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/api/llm",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"llm_id": llm_id}, llm_delete_params.LlmDeleteParams),
            ),
            cast_to=object,
        )

    def create_or_update(
        self,
        *,
        llm_id: Optional[str] | NotGiven = NOT_GIVEN,
        icon: str | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        model_name: str | NotGiven = NOT_GIVEN,
        openai_api_key: str | NotGiven = NOT_GIVEN,
        openai_base_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        创建或更新大模型配置

        Args:
          llm_id: 大模型 ID

          icon: 图标

          max_tokens: 最大 token 数

          model_name: 模型名称

          openai_api_key: OpenAI API Key

          openai_base_url: OpenAI API Base URL

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/api/llm",
            body=maybe_transform(
                {
                    "icon": icon,
                    "max_tokens": max_tokens,
                    "model_name": model_name,
                    "openai_api_key": openai_api_key,
                    "openai_base_url": openai_base_url,
                },
                llm_create_or_update_params.LlmCreateOrUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"llm_id": llm_id}, llm_create_or_update_params.LlmCreateOrUpdateParams),
            ),
            cast_to=object,
        )

    def list_providers(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LlmListProvidersResponse:
        """获取大模型提供商列表"""
        return self._get(
            "/api/llm/provider",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LlmListProvidersResponse,
        )

    def update_conv(
        self,
        *,
        conversation_id: str,
        llm_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        更新对话的知识库

        Args:
          conversation_id: 对话 ID

          llm_id: llm ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/api/llm/conv",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "conversation_id": conversation_id,
                        "llm_id": llm_id,
                    },
                    llm_update_conv_params.LlmUpdateConvParams,
                ),
            ),
            cast_to=object,
        )


class AsyncLlmResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLlmResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/openhermes-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLlmResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLlmResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/openhermes-python#with_streaming_response
        """
        return AsyncLlmResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        llm_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LlmListResponse:
        """
        获取大模型列表

        Args:
          llm_id: 大模型 ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/llm",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"llm_id": llm_id}, llm_list_params.LlmListParams),
            ),
            cast_to=LlmListResponse,
        )

    async def delete(
        self,
        *,
        llm_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        删除大模型配置

        Args:
          llm_id: 大模型 ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/api/llm",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"llm_id": llm_id}, llm_delete_params.LlmDeleteParams),
            ),
            cast_to=object,
        )

    async def create_or_update(
        self,
        *,
        llm_id: Optional[str] | NotGiven = NOT_GIVEN,
        icon: str | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        model_name: str | NotGiven = NOT_GIVEN,
        openai_api_key: str | NotGiven = NOT_GIVEN,
        openai_base_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        创建或更新大模型配置

        Args:
          llm_id: 大模型 ID

          icon: 图标

          max_tokens: 最大 token 数

          model_name: 模型名称

          openai_api_key: OpenAI API Key

          openai_base_url: OpenAI API Base URL

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/api/llm",
            body=await async_maybe_transform(
                {
                    "icon": icon,
                    "max_tokens": max_tokens,
                    "model_name": model_name,
                    "openai_api_key": openai_api_key,
                    "openai_base_url": openai_base_url,
                },
                llm_create_or_update_params.LlmCreateOrUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"llm_id": llm_id}, llm_create_or_update_params.LlmCreateOrUpdateParams
                ),
            ),
            cast_to=object,
        )

    async def list_providers(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LlmListProvidersResponse:
        """获取大模型提供商列表"""
        return await self._get(
            "/api/llm/provider",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LlmListProvidersResponse,
        )

    async def update_conv(
        self,
        *,
        conversation_id: str,
        llm_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        更新对话的知识库

        Args:
          conversation_id: 对话 ID

          llm_id: llm ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/api/llm/conv",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "conversation_id": conversation_id,
                        "llm_id": llm_id,
                    },
                    llm_update_conv_params.LlmUpdateConvParams,
                ),
            ),
            cast_to=object,
        )


class LlmResourceWithRawResponse:
    def __init__(self, llm: LlmResource) -> None:
        self._llm = llm

        self.list = to_raw_response_wrapper(
            llm.list,
        )
        self.delete = to_raw_response_wrapper(
            llm.delete,
        )
        self.create_or_update = to_raw_response_wrapper(
            llm.create_or_update,
        )
        self.list_providers = to_raw_response_wrapper(
            llm.list_providers,
        )
        self.update_conv = to_raw_response_wrapper(
            llm.update_conv,
        )


class AsyncLlmResourceWithRawResponse:
    def __init__(self, llm: AsyncLlmResource) -> None:
        self._llm = llm

        self.list = async_to_raw_response_wrapper(
            llm.list,
        )
        self.delete = async_to_raw_response_wrapper(
            llm.delete,
        )
        self.create_or_update = async_to_raw_response_wrapper(
            llm.create_or_update,
        )
        self.list_providers = async_to_raw_response_wrapper(
            llm.list_providers,
        )
        self.update_conv = async_to_raw_response_wrapper(
            llm.update_conv,
        )


class LlmResourceWithStreamingResponse:
    def __init__(self, llm: LlmResource) -> None:
        self._llm = llm

        self.list = to_streamed_response_wrapper(
            llm.list,
        )
        self.delete = to_streamed_response_wrapper(
            llm.delete,
        )
        self.create_or_update = to_streamed_response_wrapper(
            llm.create_or_update,
        )
        self.list_providers = to_streamed_response_wrapper(
            llm.list_providers,
        )
        self.update_conv = to_streamed_response_wrapper(
            llm.update_conv,
        )


class AsyncLlmResourceWithStreamingResponse:
    def __init__(self, llm: AsyncLlmResource) -> None:
        self._llm = llm

        self.list = async_to_streamed_response_wrapper(
            llm.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            llm.delete,
        )
        self.create_or_update = async_to_streamed_response_wrapper(
            llm.create_or_update,
        )
        self.list_providers = async_to_streamed_response_wrapper(
            llm.list_providers,
        )
        self.update_conv = async_to_streamed_response_wrapper(
            llm.update_conv,
        )
