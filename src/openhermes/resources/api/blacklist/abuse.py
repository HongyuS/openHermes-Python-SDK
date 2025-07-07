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
from ....types.api.blacklist import abuse_get_params, abuse_change_params
from ....types.api.response_data import ResponseData
from ....types.api.blacklist.get_blacklist_question import GetBlacklistQuestion

__all__ = ["AbuseResource", "AsyncAbuseResource"]


class AbuseResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AbuseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/openhermes-python#accessing-raw-response-data-eg-headers
        """
        return AbuseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AbuseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/openhermes-python#with_streaming_response
        """
        return AbuseResourceWithStreamingResponse(self)

    def change(
        self,
        *,
        id: str,
        is_deletion: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResponseData:
        """
        对被举报问答对进行操作

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/blacklist/abuse",
            body=maybe_transform(
                {
                    "id": id,
                    "is_deletion": is_deletion,
                },
                abuse_change_params.AbuseChangeParams,
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
    ) -> GetBlacklistQuestion:
        """
        获取待审核的问答对

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/blacklist/abuse",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"page": page}, abuse_get_params.AbuseGetParams),
            ),
            cast_to=GetBlacklistQuestion,
        )


class AsyncAbuseResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAbuseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/openhermes-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAbuseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAbuseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/openhermes-python#with_streaming_response
        """
        return AsyncAbuseResourceWithStreamingResponse(self)

    async def change(
        self,
        *,
        id: str,
        is_deletion: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResponseData:
        """
        对被举报问答对进行操作

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/blacklist/abuse",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "is_deletion": is_deletion,
                },
                abuse_change_params.AbuseChangeParams,
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
    ) -> GetBlacklistQuestion:
        """
        获取待审核的问答对

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/blacklist/abuse",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"page": page}, abuse_get_params.AbuseGetParams),
            ),
            cast_to=GetBlacklistQuestion,
        )


class AbuseResourceWithRawResponse:
    def __init__(self, abuse: AbuseResource) -> None:
        self._abuse = abuse

        self.change = to_raw_response_wrapper(
            abuse.change,
        )
        self.get = to_raw_response_wrapper(
            abuse.get,
        )


class AsyncAbuseResourceWithRawResponse:
    def __init__(self, abuse: AsyncAbuseResource) -> None:
        self._abuse = abuse

        self.change = async_to_raw_response_wrapper(
            abuse.change,
        )
        self.get = async_to_raw_response_wrapper(
            abuse.get,
        )


class AbuseResourceWithStreamingResponse:
    def __init__(self, abuse: AbuseResource) -> None:
        self._abuse = abuse

        self.change = to_streamed_response_wrapper(
            abuse.change,
        )
        self.get = to_streamed_response_wrapper(
            abuse.get,
        )


class AsyncAbuseResourceWithStreamingResponse:
    def __init__(self, abuse: AsyncAbuseResource) -> None:
        self._abuse = abuse

        self.change = async_to_streamed_response_wrapper(
            abuse.change,
        )
        self.get = async_to_streamed_response_wrapper(
            abuse.get,
        )
