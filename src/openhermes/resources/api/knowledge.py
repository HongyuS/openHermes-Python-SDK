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
from ...types.api import knowledge_list_params, knowledge_update_params
from ..._base_client import make_request_options
from ...types.api.response_data import ResponseData
from ...types.api.knowledge_list_response import KnowledgeListResponse

__all__ = ["KnowledgeResource", "AsyncKnowledgeResource"]


class KnowledgeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> KnowledgeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HongyuS/openHermes-Python-SDK#accessing-raw-response-data-eg-headers
        """
        return KnowledgeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KnowledgeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HongyuS/openHermes-Python-SDK#with_streaming_response
        """
        return KnowledgeResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        conversation_id: str,
        kb_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResponseData:
        """
        更新当前用户的知识库 ID

        Args:
          kb_ids: 知识库 ID 列表

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/api/knowledge",
            body=maybe_transform({"kb_ids": kb_ids}, knowledge_update_params.KnowledgeUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"conversation_id": conversation_id}, knowledge_update_params.KnowledgeUpdateParams
                ),
            ),
            cast_to=ResponseData,
        )

    def list(
        self,
        *,
        conversation_id: str,
        kb_id: str | NotGiven = NOT_GIVEN,
        kb_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KnowledgeListResponse:
        """
        获取当前用户的知识库 ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/knowledge",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "conversation_id": conversation_id,
                        "kb_id": kb_id,
                        "kb_name": kb_name,
                    },
                    knowledge_list_params.KnowledgeListParams,
                ),
            ),
            cast_to=KnowledgeListResponse,
        )


class AsyncKnowledgeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncKnowledgeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HongyuS/openHermes-Python-SDK#accessing-raw-response-data-eg-headers
        """
        return AsyncKnowledgeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKnowledgeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HongyuS/openHermes-Python-SDK#with_streaming_response
        """
        return AsyncKnowledgeResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        conversation_id: str,
        kb_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResponseData:
        """
        更新当前用户的知识库 ID

        Args:
          kb_ids: 知识库 ID 列表

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/api/knowledge",
            body=await async_maybe_transform({"kb_ids": kb_ids}, knowledge_update_params.KnowledgeUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"conversation_id": conversation_id}, knowledge_update_params.KnowledgeUpdateParams
                ),
            ),
            cast_to=ResponseData,
        )

    async def list(
        self,
        *,
        conversation_id: str,
        kb_id: str | NotGiven = NOT_GIVEN,
        kb_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KnowledgeListResponse:
        """
        获取当前用户的知识库 ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/knowledge",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "conversation_id": conversation_id,
                        "kb_id": kb_id,
                        "kb_name": kb_name,
                    },
                    knowledge_list_params.KnowledgeListParams,
                ),
            ),
            cast_to=KnowledgeListResponse,
        )


class KnowledgeResourceWithRawResponse:
    def __init__(self, knowledge: KnowledgeResource) -> None:
        self._knowledge = knowledge

        self.update = to_raw_response_wrapper(
            knowledge.update,
        )
        self.list = to_raw_response_wrapper(
            knowledge.list,
        )


class AsyncKnowledgeResourceWithRawResponse:
    def __init__(self, knowledge: AsyncKnowledgeResource) -> None:
        self._knowledge = knowledge

        self.update = async_to_raw_response_wrapper(
            knowledge.update,
        )
        self.list = async_to_raw_response_wrapper(
            knowledge.list,
        )


class KnowledgeResourceWithStreamingResponse:
    def __init__(self, knowledge: KnowledgeResource) -> None:
        self._knowledge = knowledge

        self.update = to_streamed_response_wrapper(
            knowledge.update,
        )
        self.list = to_streamed_response_wrapper(
            knowledge.list,
        )


class AsyncKnowledgeResourceWithStreamingResponse:
    def __init__(self, knowledge: AsyncKnowledgeResource) -> None:
        self._knowledge = knowledge

        self.update = async_to_streamed_response_wrapper(
            knowledge.update,
        )
        self.list = async_to_streamed_response_wrapper(
            knowledge.list,
        )
