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
from ....types.api.auth import logout_post_params
from ....types.api.response_data import ResponseData

__all__ = ["LogoutResource", "AsyncLogoutResource"]


class LogoutResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LogoutResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HongyuS/openHermes-Python-SDK#accessing-raw-response-data-eg-headers
        """
        return LogoutResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LogoutResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HongyuS/openHermes-Python-SDK#with_streaming_response
        """
        return LogoutResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResponseData:
        """用户登出 EulerCopilot"""
        return self._get(
            "/api/auth/logout",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseData,
        )

    def post(
        self,
        *,
        token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResponseData:
        """
        OIDC 主动触发登出

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/auth/logout",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"token": token}, logout_post_params.LogoutPostParams),
            ),
            cast_to=ResponseData,
        )


class AsyncLogoutResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLogoutResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HongyuS/openHermes-Python-SDK#accessing-raw-response-data-eg-headers
        """
        return AsyncLogoutResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLogoutResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HongyuS/openHermes-Python-SDK#with_streaming_response
        """
        return AsyncLogoutResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResponseData:
        """用户登出 EulerCopilot"""
        return await self._get(
            "/api/auth/logout",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseData,
        )

    async def post(
        self,
        *,
        token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResponseData:
        """
        OIDC 主动触发登出

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/auth/logout",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"token": token}, logout_post_params.LogoutPostParams),
            ),
            cast_to=ResponseData,
        )


class LogoutResourceWithRawResponse:
    def __init__(self, logout: LogoutResource) -> None:
        self._logout = logout

        self.get = to_raw_response_wrapper(
            logout.get,
        )
        self.post = to_raw_response_wrapper(
            logout.post,
        )


class AsyncLogoutResourceWithRawResponse:
    def __init__(self, logout: AsyncLogoutResource) -> None:
        self._logout = logout

        self.get = async_to_raw_response_wrapper(
            logout.get,
        )
        self.post = async_to_raw_response_wrapper(
            logout.post,
        )


class LogoutResourceWithStreamingResponse:
    def __init__(self, logout: LogoutResource) -> None:
        self._logout = logout

        self.get = to_streamed_response_wrapper(
            logout.get,
        )
        self.post = to_streamed_response_wrapper(
            logout.post,
        )


class AsyncLogoutResourceWithStreamingResponse:
    def __init__(self, logout: AsyncLogoutResource) -> None:
        self._logout = logout

        self.get = async_to_streamed_response_wrapper(
            logout.get,
        )
        self.post = async_to_streamed_response_wrapper(
            logout.post,
        )
