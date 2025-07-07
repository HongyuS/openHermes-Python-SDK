# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.health_check_check_response import HealthCheckCheckResponse

__all__ = ["HealthCheckResource", "AsyncHealthCheckResource"]


class HealthCheckResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HealthCheckResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/openhermes-python#accessing-raw-response-data-eg-headers
        """
        return HealthCheckResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HealthCheckResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/openhermes-python#with_streaming_response
        """
        return HealthCheckResourceWithStreamingResponse(self)

    def check(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HealthCheckCheckResponse:
        """健康检查接口"""
        return self._get(
            "/health_check",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HealthCheckCheckResponse,
        )


class AsyncHealthCheckResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHealthCheckResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/openhermes-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHealthCheckResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHealthCheckResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/openhermes-python#with_streaming_response
        """
        return AsyncHealthCheckResourceWithStreamingResponse(self)

    async def check(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HealthCheckCheckResponse:
        """健康检查接口"""
        return await self._get(
            "/health_check",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HealthCheckCheckResponse,
        )


class HealthCheckResourceWithRawResponse:
    def __init__(self, health_check: HealthCheckResource) -> None:
        self._health_check = health_check

        self.check = to_raw_response_wrapper(
            health_check.check,
        )


class AsyncHealthCheckResourceWithRawResponse:
    def __init__(self, health_check: AsyncHealthCheckResource) -> None:
        self._health_check = health_check

        self.check = async_to_raw_response_wrapper(
            health_check.check,
        )


class HealthCheckResourceWithStreamingResponse:
    def __init__(self, health_check: HealthCheckResource) -> None:
        self._health_check = health_check

        self.check = to_streamed_response_wrapper(
            health_check.check,
        )


class AsyncHealthCheckResourceWithStreamingResponse:
    def __init__(self, health_check: AsyncHealthCheckResource) -> None:
        self._health_check = health_check

        self.check = async_to_streamed_response_wrapper(
            health_check.check,
        )
