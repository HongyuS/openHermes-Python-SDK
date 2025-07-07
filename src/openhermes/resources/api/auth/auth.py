# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .key import (
    KeyResource,
    AsyncKeyResource,
    KeyResourceWithRawResponse,
    AsyncKeyResourceWithRawResponse,
    KeyResourceWithStreamingResponse,
    AsyncKeyResourceWithStreamingResponse,
)
from .logout import (
    LogoutResource,
    AsyncLogoutResource,
    LogoutResourceWithRawResponse,
    AsyncLogoutResourceWithRawResponse,
    LogoutResourceWithStreamingResponse,
    AsyncLogoutResourceWithStreamingResponse,
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
from ....types.api import auth_login_params
from ...._base_client import make_request_options
from ....types.api.auth_user_rsp import AuthUserRsp
from ....types.api.auth_redirect_response import AuthRedirectResponse

__all__ = ["AuthResource", "AsyncAuthResource"]


class AuthResource(SyncAPIResource):
    @cached_property
    def logout(self) -> LogoutResource:
        return LogoutResource(self._client)

    @cached_property
    def key(self) -> KeyResource:
        return KeyResource(self._client)

    @cached_property
    def with_raw_response(self) -> AuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HongyuS/openHermes-Python-SDK#accessing-raw-response-data-eg-headers
        """
        return AuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HongyuS/openHermes-Python-SDK#with_streaming_response
        """
        return AuthResourceWithStreamingResponse(self)

    def login(
        self,
        *,
        code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        OIDC login

        :param request: Request object :param code: OIDC code :return: HTMLResponse

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/auth/login",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"code": code}, auth_login_params.AuthLoginParams),
            ),
            cast_to=object,
        )

    def redirect(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthRedirectResponse:
        """OIDC 重定向 URL"""
        return self._get(
            "/api/auth/redirect",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthRedirectResponse,
        )

    def retrieve_user(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthUserRsp:
        """获取用户信息"""
        return self._get(
            "/api/auth/user",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthUserRsp,
        )

    def update_revision(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthUserRsp:
        """更新用户协议信息"""
        return self._post(
            "/api/auth/update_revision_number",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthUserRsp,
        )


class AsyncAuthResource(AsyncAPIResource):
    @cached_property
    def logout(self) -> AsyncLogoutResource:
        return AsyncLogoutResource(self._client)

    @cached_property
    def key(self) -> AsyncKeyResource:
        return AsyncKeyResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HongyuS/openHermes-Python-SDK#accessing-raw-response-data-eg-headers
        """
        return AsyncAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HongyuS/openHermes-Python-SDK#with_streaming_response
        """
        return AsyncAuthResourceWithStreamingResponse(self)

    async def login(
        self,
        *,
        code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        OIDC login

        :param request: Request object :param code: OIDC code :return: HTMLResponse

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/auth/login",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"code": code}, auth_login_params.AuthLoginParams),
            ),
            cast_to=object,
        )

    async def redirect(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthRedirectResponse:
        """OIDC 重定向 URL"""
        return await self._get(
            "/api/auth/redirect",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthRedirectResponse,
        )

    async def retrieve_user(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthUserRsp:
        """获取用户信息"""
        return await self._get(
            "/api/auth/user",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthUserRsp,
        )

    async def update_revision(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthUserRsp:
        """更新用户协议信息"""
        return await self._post(
            "/api/auth/update_revision_number",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthUserRsp,
        )


class AuthResourceWithRawResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

        self.login = to_raw_response_wrapper(
            auth.login,
        )
        self.redirect = to_raw_response_wrapper(
            auth.redirect,
        )
        self.retrieve_user = to_raw_response_wrapper(
            auth.retrieve_user,
        )
        self.update_revision = to_raw_response_wrapper(
            auth.update_revision,
        )

    @cached_property
    def logout(self) -> LogoutResourceWithRawResponse:
        return LogoutResourceWithRawResponse(self._auth.logout)

    @cached_property
    def key(self) -> KeyResourceWithRawResponse:
        return KeyResourceWithRawResponse(self._auth.key)


class AsyncAuthResourceWithRawResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

        self.login = async_to_raw_response_wrapper(
            auth.login,
        )
        self.redirect = async_to_raw_response_wrapper(
            auth.redirect,
        )
        self.retrieve_user = async_to_raw_response_wrapper(
            auth.retrieve_user,
        )
        self.update_revision = async_to_raw_response_wrapper(
            auth.update_revision,
        )

    @cached_property
    def logout(self) -> AsyncLogoutResourceWithRawResponse:
        return AsyncLogoutResourceWithRawResponse(self._auth.logout)

    @cached_property
    def key(self) -> AsyncKeyResourceWithRawResponse:
        return AsyncKeyResourceWithRawResponse(self._auth.key)


class AuthResourceWithStreamingResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

        self.login = to_streamed_response_wrapper(
            auth.login,
        )
        self.redirect = to_streamed_response_wrapper(
            auth.redirect,
        )
        self.retrieve_user = to_streamed_response_wrapper(
            auth.retrieve_user,
        )
        self.update_revision = to_streamed_response_wrapper(
            auth.update_revision,
        )

    @cached_property
    def logout(self) -> LogoutResourceWithStreamingResponse:
        return LogoutResourceWithStreamingResponse(self._auth.logout)

    @cached_property
    def key(self) -> KeyResourceWithStreamingResponse:
        return KeyResourceWithStreamingResponse(self._auth.key)


class AsyncAuthResourceWithStreamingResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

        self.login = async_to_streamed_response_wrapper(
            auth.login,
        )
        self.redirect = async_to_streamed_response_wrapper(
            auth.redirect,
        )
        self.retrieve_user = async_to_streamed_response_wrapper(
            auth.retrieve_user,
        )
        self.update_revision = async_to_streamed_response_wrapper(
            auth.update_revision,
        )

    @cached_property
    def logout(self) -> AsyncLogoutResourceWithStreamingResponse:
        return AsyncLogoutResourceWithStreamingResponse(self._auth.logout)

    @cached_property
    def key(self) -> AsyncKeyResourceWithStreamingResponse:
        return AsyncKeyResourceWithStreamingResponse(self._auth.key)
