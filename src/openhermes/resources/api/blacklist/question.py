# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.api.blacklist import question_get_params, question_change_params
from ....types.api.response_data import ResponseData
from ....types.api.blacklist.get_blacklist_question_rsp import GetBlacklistQuestionRsp

__all__ = ["QuestionResource", "AsyncQuestionResource"]


class QuestionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> QuestionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HongyuS/openHermes-Python-SDK#accessing-raw-response-data-eg-headers
        """
        return QuestionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QuestionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HongyuS/openHermes-Python-SDK#with_streaming_response
        """
        return QuestionResourceWithStreamingResponse(self)

    def change(
        self,
        *,
        id: str,
        answer: str,
        is_deletion: int,
        question: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResponseData:
        """
        黑名单问题检测或操作

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/blacklist/question",
            body=maybe_transform(
                {
                    "id": id,
                    "answer": answer,
                    "is_deletion": is_deletion,
                    "question": question,
                },
                question_change_params.QuestionChangeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseData,
        )

    def get(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GetBlacklistQuestionRsp:
        """
        获取黑名单问题

        目前情况下，先直接输出问题，不做用户类型校验

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/blacklist/question",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"page": page}, question_get_params.QuestionGetParams),
            ),
            cast_to=GetBlacklistQuestionRsp,
        )


class AsyncQuestionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQuestionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HongyuS/openHermes-Python-SDK#accessing-raw-response-data-eg-headers
        """
        return AsyncQuestionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQuestionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HongyuS/openHermes-Python-SDK#with_streaming_response
        """
        return AsyncQuestionResourceWithStreamingResponse(self)

    async def change(
        self,
        *,
        id: str,
        answer: str,
        is_deletion: int,
        question: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResponseData:
        """
        黑名单问题检测或操作

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/blacklist/question",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "answer": answer,
                    "is_deletion": is_deletion,
                    "question": question,
                },
                question_change_params.QuestionChangeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseData,
        )

    async def get(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GetBlacklistQuestionRsp:
        """
        获取黑名单问题

        目前情况下，先直接输出问题，不做用户类型校验

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/blacklist/question",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"page": page}, question_get_params.QuestionGetParams),
            ),
            cast_to=GetBlacklistQuestionRsp,
        )


class QuestionResourceWithRawResponse:
    def __init__(self, question: QuestionResource) -> None:
        self._question = question

        self.change = to_raw_response_wrapper(
            question.change,
        )
        self.get = to_raw_response_wrapper(
            question.get,
        )


class AsyncQuestionResourceWithRawResponse:
    def __init__(self, question: AsyncQuestionResource) -> None:
        self._question = question

        self.change = async_to_raw_response_wrapper(
            question.change,
        )
        self.get = async_to_raw_response_wrapper(
            question.get,
        )


class QuestionResourceWithStreamingResponse:
    def __init__(self, question: QuestionResource) -> None:
        self._question = question

        self.change = to_streamed_response_wrapper(
            question.change,
        )
        self.get = to_streamed_response_wrapper(
            question.get,
        )


class AsyncQuestionResourceWithStreamingResponse:
    def __init__(self, question: AsyncQuestionResource) -> None:
        self._question = question

        self.change = async_to_streamed_response_wrapper(
            question.change,
        )
        self.get = async_to_streamed_response_wrapper(
            question.get,
        )
