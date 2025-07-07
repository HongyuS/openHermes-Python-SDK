# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .user import (
    UserResource,
    AsyncUserResource,
    UserResourceWithRawResponse,
    AsyncUserResourceWithRawResponse,
    UserResourceWithStreamingResponse,
    AsyncUserResourceWithStreamingResponse,
)
from .abuse import (
    AbuseResource,
    AsyncAbuseResource,
    AbuseResourceWithRawResponse,
    AsyncAbuseResourceWithRawResponse,
    AbuseResourceWithStreamingResponse,
    AsyncAbuseResourceWithStreamingResponse,
)
from .question import (
    QuestionResource,
    AsyncQuestionResource,
    QuestionResourceWithRawResponse,
    AsyncQuestionResourceWithRawResponse,
    QuestionResourceWithStreamingResponse,
    AsyncQuestionResourceWithStreamingResponse,
)
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
from ....types.api import blacklist_report_abuse_params
from ...._base_client import make_request_options
from ....types.api.response_data import ResponseData

__all__ = ["BlacklistResource", "AsyncBlacklistResource"]


class BlacklistResource(SyncAPIResource):
    @cached_property
    def user(self) -> UserResource:
        return UserResource(self._client)

    @cached_property
    def question(self) -> QuestionResource:
        return QuestionResource(self._client)

    @cached_property
    def abuse(self) -> AbuseResource:
        return AbuseResource(self._client)

    @cached_property
    def with_raw_response(self) -> BlacklistResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HongyuS/openHermes-Python-SDK#accessing-raw-response-data-eg-headers
        """
        return BlacklistResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BlacklistResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HongyuS/openHermes-Python-SDK#with_streaming_response
        """
        return BlacklistResourceWithStreamingResponse(self)

    def report_abuse(
        self,
        *,
        reason: str,
        reason_type: str,
        record_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResponseData:
        """
        用户实施举报

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/blacklist/complaint",
            body=maybe_transform(
                {
                    "reason": reason,
                    "reason_type": reason_type,
                    "record_id": record_id,
                },
                blacklist_report_abuse_params.BlacklistReportAbuseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseData,
        )


class AsyncBlacklistResource(AsyncAPIResource):
    @cached_property
    def user(self) -> AsyncUserResource:
        return AsyncUserResource(self._client)

    @cached_property
    def question(self) -> AsyncQuestionResource:
        return AsyncQuestionResource(self._client)

    @cached_property
    def abuse(self) -> AsyncAbuseResource:
        return AsyncAbuseResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBlacklistResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HongyuS/openHermes-Python-SDK#accessing-raw-response-data-eg-headers
        """
        return AsyncBlacklistResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBlacklistResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HongyuS/openHermes-Python-SDK#with_streaming_response
        """
        return AsyncBlacklistResourceWithStreamingResponse(self)

    async def report_abuse(
        self,
        *,
        reason: str,
        reason_type: str,
        record_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResponseData:
        """
        用户实施举报

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/blacklist/complaint",
            body=await async_maybe_transform(
                {
                    "reason": reason,
                    "reason_type": reason_type,
                    "record_id": record_id,
                },
                blacklist_report_abuse_params.BlacklistReportAbuseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseData,
        )


class BlacklistResourceWithRawResponse:
    def __init__(self, blacklist: BlacklistResource) -> None:
        self._blacklist = blacklist

        self.report_abuse = to_raw_response_wrapper(
            blacklist.report_abuse,
        )

    @cached_property
    def user(self) -> UserResourceWithRawResponse:
        return UserResourceWithRawResponse(self._blacklist.user)

    @cached_property
    def question(self) -> QuestionResourceWithRawResponse:
        return QuestionResourceWithRawResponse(self._blacklist.question)

    @cached_property
    def abuse(self) -> AbuseResourceWithRawResponse:
        return AbuseResourceWithRawResponse(self._blacklist.abuse)


class AsyncBlacklistResourceWithRawResponse:
    def __init__(self, blacklist: AsyncBlacklistResource) -> None:
        self._blacklist = blacklist

        self.report_abuse = async_to_raw_response_wrapper(
            blacklist.report_abuse,
        )

    @cached_property
    def user(self) -> AsyncUserResourceWithRawResponse:
        return AsyncUserResourceWithRawResponse(self._blacklist.user)

    @cached_property
    def question(self) -> AsyncQuestionResourceWithRawResponse:
        return AsyncQuestionResourceWithRawResponse(self._blacklist.question)

    @cached_property
    def abuse(self) -> AsyncAbuseResourceWithRawResponse:
        return AsyncAbuseResourceWithRawResponse(self._blacklist.abuse)


class BlacklistResourceWithStreamingResponse:
    def __init__(self, blacklist: BlacklistResource) -> None:
        self._blacklist = blacklist

        self.report_abuse = to_streamed_response_wrapper(
            blacklist.report_abuse,
        )

    @cached_property
    def user(self) -> UserResourceWithStreamingResponse:
        return UserResourceWithStreamingResponse(self._blacklist.user)

    @cached_property
    def question(self) -> QuestionResourceWithStreamingResponse:
        return QuestionResourceWithStreamingResponse(self._blacklist.question)

    @cached_property
    def abuse(self) -> AbuseResourceWithStreamingResponse:
        return AbuseResourceWithStreamingResponse(self._blacklist.abuse)


class AsyncBlacklistResourceWithStreamingResponse:
    def __init__(self, blacklist: AsyncBlacklistResource) -> None:
        self._blacklist = blacklist

        self.report_abuse = async_to_streamed_response_wrapper(
            blacklist.report_abuse,
        )

    @cached_property
    def user(self) -> AsyncUserResourceWithStreamingResponse:
        return AsyncUserResourceWithStreamingResponse(self._blacklist.user)

    @cached_property
    def question(self) -> AsyncQuestionResourceWithStreamingResponse:
        return AsyncQuestionResourceWithStreamingResponse(self._blacklist.question)

    @cached_property
    def abuse(self) -> AsyncAbuseResourceWithStreamingResponse:
        return AsyncAbuseResourceWithStreamingResponse(self._blacklist.abuse)
