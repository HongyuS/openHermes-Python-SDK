# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

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
from ...types.api import conversation_create_params, conversation_delete_params, conversation_update_params
from ..._base_client import make_request_options
from ...types.api.response_data import ResponseData
from ...types.api.conversation_list_response import ConversationListResponse
from ...types.api.conversation_create_response import ConversationCreateResponse
from ...types.api.conversation_update_response import ConversationUpdateResponse

__all__ = ["ConversationResource", "AsyncConversationResource"]


class ConversationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConversationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/openhermes-python#accessing-raw-response-data-eg-headers
        """
        return ConversationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConversationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/openhermes-python#with_streaming_response
        """
        return ConversationResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        app_id: str | NotGiven = NOT_GIVEN,
        debug: bool | NotGiven = NOT_GIVEN,
        kb_ids: List[str] | NotGiven = NOT_GIVEN,
        llm_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConversationCreateResponse:
        """
        手动创建新对话

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/conversation",
            body=maybe_transform(
                {
                    "kb_ids": kb_ids,
                    "llm_id": llm_id,
                },
                conversation_create_params.ConversationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "app_id": app_id,
                        "debug": debug,
                    },
                    conversation_create_params.ConversationCreateParams,
                ),
            ),
            cast_to=ConversationCreateResponse,
        )

    def update(
        self,
        *,
        conversation_id: str,
        title: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConversationUpdateResponse:
        """
        更新特定 Conversation 的数据

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/api/conversation",
            body=maybe_transform({"title": title}, conversation_update_params.ConversationUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"conversation_id": conversation_id}, conversation_update_params.ConversationUpdateParams
                ),
            ),
            cast_to=ConversationUpdateResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConversationListResponse:
        """获取对话列表"""
        return self._get(
            "/api/conversation",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationListResponse,
        )

    def delete(
        self,
        *,
        conversation_list: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResponseData:
        """
        删除特定对话

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/api/conversation",
            body=maybe_transform(
                {"conversation_list": conversation_list}, conversation_delete_params.ConversationDeleteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseData,
        )


class AsyncConversationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConversationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/openhermes-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConversationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConversationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/openhermes-python#with_streaming_response
        """
        return AsyncConversationResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        app_id: str | NotGiven = NOT_GIVEN,
        debug: bool | NotGiven = NOT_GIVEN,
        kb_ids: List[str] | NotGiven = NOT_GIVEN,
        llm_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConversationCreateResponse:
        """
        手动创建新对话

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/conversation",
            body=await async_maybe_transform(
                {
                    "kb_ids": kb_ids,
                    "llm_id": llm_id,
                },
                conversation_create_params.ConversationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "app_id": app_id,
                        "debug": debug,
                    },
                    conversation_create_params.ConversationCreateParams,
                ),
            ),
            cast_to=ConversationCreateResponse,
        )

    async def update(
        self,
        *,
        conversation_id: str,
        title: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConversationUpdateResponse:
        """
        更新特定 Conversation 的数据

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/api/conversation",
            body=await async_maybe_transform({"title": title}, conversation_update_params.ConversationUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"conversation_id": conversation_id}, conversation_update_params.ConversationUpdateParams
                ),
            ),
            cast_to=ConversationUpdateResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConversationListResponse:
        """获取对话列表"""
        return await self._get(
            "/api/conversation",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationListResponse,
        )

    async def delete(
        self,
        *,
        conversation_list: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResponseData:
        """
        删除特定对话

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/api/conversation",
            body=await async_maybe_transform(
                {"conversation_list": conversation_list}, conversation_delete_params.ConversationDeleteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseData,
        )


class ConversationResourceWithRawResponse:
    def __init__(self, conversation: ConversationResource) -> None:
        self._conversation = conversation

        self.create = to_raw_response_wrapper(
            conversation.create,
        )
        self.update = to_raw_response_wrapper(
            conversation.update,
        )
        self.list = to_raw_response_wrapper(
            conversation.list,
        )
        self.delete = to_raw_response_wrapper(
            conversation.delete,
        )


class AsyncConversationResourceWithRawResponse:
    def __init__(self, conversation: AsyncConversationResource) -> None:
        self._conversation = conversation

        self.create = async_to_raw_response_wrapper(
            conversation.create,
        )
        self.update = async_to_raw_response_wrapper(
            conversation.update,
        )
        self.list = async_to_raw_response_wrapper(
            conversation.list,
        )
        self.delete = async_to_raw_response_wrapper(
            conversation.delete,
        )


class ConversationResourceWithStreamingResponse:
    def __init__(self, conversation: ConversationResource) -> None:
        self._conversation = conversation

        self.create = to_streamed_response_wrapper(
            conversation.create,
        )
        self.update = to_streamed_response_wrapper(
            conversation.update,
        )
        self.list = to_streamed_response_wrapper(
            conversation.list,
        )
        self.delete = to_streamed_response_wrapper(
            conversation.delete,
        )


class AsyncConversationResourceWithStreamingResponse:
    def __init__(self, conversation: AsyncConversationResource) -> None:
        self._conversation = conversation

        self.create = async_to_streamed_response_wrapper(
            conversation.create,
        )
        self.update = async_to_streamed_response_wrapper(
            conversation.update,
        )
        self.list = async_to_streamed_response_wrapper(
            conversation.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            conversation.delete,
        )
