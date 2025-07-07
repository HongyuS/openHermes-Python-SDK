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
from ....types.api.auth import key_manage_params
from ....types.api.auth.key_check_response import KeyCheckResponse
from ....types.api.auth.key_manage_response import KeyManageResponse

__all__ = ["KeyResource", "AsyncKeyResource"]


class KeyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> KeyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/openhermes-python#accessing-raw-response-data-eg-headers
        """
        return KeyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KeyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/openhermes-python#with_streaming_response
        """
        return KeyResourceWithStreamingResponse(self)

    def check(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KeyCheckResponse:
        """检查 API 密钥是否存在"""
        return self._get(
            "/api/auth/key",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeyCheckResponse,
        )

    def manage(
        self,
        *,
        action: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KeyManageResponse:
        """
        管理用户的 API 密钥

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/auth/key",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"action": action}, key_manage_params.KeyManageParams),
            ),
            cast_to=KeyManageResponse,
        )


class AsyncKeyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncKeyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/openhermes-python#accessing-raw-response-data-eg-headers
        """
        return AsyncKeyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKeyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/openhermes-python#with_streaming_response
        """
        return AsyncKeyResourceWithStreamingResponse(self)

    async def check(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KeyCheckResponse:
        """检查 API 密钥是否存在"""
        return await self._get(
            "/api/auth/key",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeyCheckResponse,
        )

    async def manage(
        self,
        *,
        action: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KeyManageResponse:
        """
        管理用户的 API 密钥

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/auth/key",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"action": action}, key_manage_params.KeyManageParams),
            ),
            cast_to=KeyManageResponse,
        )


class KeyResourceWithRawResponse:
    def __init__(self, key: KeyResource) -> None:
        self._key = key

        self.check = to_raw_response_wrapper(
            key.check,
        )
        self.manage = to_raw_response_wrapper(
            key.manage,
        )


class AsyncKeyResourceWithRawResponse:
    def __init__(self, key: AsyncKeyResource) -> None:
        self._key = key

        self.check = async_to_raw_response_wrapper(
            key.check,
        )
        self.manage = async_to_raw_response_wrapper(
            key.manage,
        )


class KeyResourceWithStreamingResponse:
    def __init__(self, key: KeyResource) -> None:
        self._key = key

        self.check = to_streamed_response_wrapper(
            key.check,
        )
        self.manage = to_streamed_response_wrapper(
            key.manage,
        )


class AsyncKeyResourceWithStreamingResponse:
    def __init__(self, key: AsyncKeyResource) -> None:
        self._key = key

        self.check = async_to_streamed_response_wrapper(
            key.check,
        )
        self.manage = async_to_streamed_response_wrapper(
            key.manage,
        )
