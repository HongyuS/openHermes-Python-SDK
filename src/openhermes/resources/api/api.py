# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

import httpx

from ... import _resource
from .app import (
    AppResource,
    AsyncAppResource,
    AppResourceWithRawResponse,
    AsyncAppResourceWithRawResponse,
    AppResourceWithStreamingResponse,
    AsyncAppResourceWithStreamingResponse,
)
from .llm import (
    LlmResource,
    AsyncLlmResource,
    LlmResourceWithRawResponse,
    AsyncLlmResourceWithRawResponse,
    LlmResourceWithStreamingResponse,
    AsyncLlmResourceWithStreamingResponse,
)
from .mcp import (
    McpResource,
    AsyncMcpResource,
    McpResourceWithRawResponse,
    AsyncMcpResourceWithRawResponse,
    McpResourceWithStreamingResponse,
    AsyncMcpResourceWithStreamingResponse,
)
from .flow import (
    FlowResource,
    AsyncFlowResource,
    FlowResourceWithRawResponse,
    AsyncFlowResourceWithRawResponse,
    FlowResourceWithStreamingResponse,
    AsyncFlowResourceWithStreamingResponse,
)
from ...types import CommentType, api_chat_params, api_add_comment_params
from .service import (
    ServiceResource,
    AsyncServiceResource,
    ServiceResourceWithRawResponse,
    AsyncServiceResourceWithRawResponse,
    ServiceResourceWithStreamingResponse,
    AsyncServiceResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from .document import (
    DocumentResource,
    AsyncDocumentResource,
    DocumentResourceWithRawResponse,
    AsyncDocumentResourceWithRawResponse,
    DocumentResourceWithStreamingResponse,
    AsyncDocumentResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .auth.auth import (
    AuthResource,
    AsyncAuthResource,
    AuthResourceWithRawResponse,
    AsyncAuthResourceWithRawResponse,
    AuthResourceWithStreamingResponse,
    AsyncAuthResourceWithStreamingResponse,
)
from .knowledge import (
    KnowledgeResource,
    AsyncKnowledgeResource,
    KnowledgeResourceWithRawResponse,
    AsyncKnowledgeResourceWithRawResponse,
    KnowledgeResourceWithStreamingResponse,
    AsyncKnowledgeResourceWithStreamingResponse,
)
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .conversation import (
    ConversationResource,
    AsyncConversationResource,
    ConversationResourceWithRawResponse,
    AsyncConversationResourceWithRawResponse,
    ConversationResourceWithStreamingResponse,
    AsyncConversationResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from .blacklist.blacklist import (
    BlacklistResource,
    AsyncBlacklistResource,
    BlacklistResourceWithRawResponse,
    AsyncBlacklistResourceWithRawResponse,
    BlacklistResourceWithStreamingResponse,
    AsyncBlacklistResourceWithStreamingResponse,
)
from ...types.comment_type import CommentType
from ...types.api.response_data import ResponseData
from ...types.api_get_record_response import APIGetRecordResponse

__all__ = ["APIResource", "AsyncAPIResource"]


class APIResource(_resource.SyncAPIResource):
    @cached_property
    def conversation(self) -> ConversationResource:
        return ConversationResource(self._client)

    @cached_property
    def auth(self) -> AuthResource:
        return AuthResource(self._client)

    @cached_property
    def app(self) -> AppResource:
        return AppResource(self._client)

    @cached_property
    def service(self) -> ServiceResource:
        return ServiceResource(self._client)

    @cached_property
    def blacklist(self) -> BlacklistResource:
        return BlacklistResource(self._client)

    @cached_property
    def document(self) -> DocumentResource:
        return DocumentResource(self._client)

    @cached_property
    def knowledge(self) -> KnowledgeResource:
        return KnowledgeResource(self._client)

    @cached_property
    def llm(self) -> LlmResource:
        return LlmResource(self._client)

    @cached_property
    def mcp(self) -> McpResource:
        return McpResource(self._client)

    @cached_property
    def flow(self) -> FlowResource:
        return FlowResource(self._client)

    @cached_property
    def with_raw_response(self) -> APIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HongyuS/openHermes-Python-SDK#accessing-raw-response-data-eg-headers
        """
        return APIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> APIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HongyuS/openHermes-Python-SDK#with_streaming_response
        """
        return APIResourceWithStreamingResponse(self)

    def add_comment(
        self,
        *,
        comment: CommentType,
        group_id: str,
        record_id: str,
        dislike_reason: str | NotGiven = NOT_GIVEN,
        reason_description: str | NotGiven = NOT_GIVEN,
        reason_link: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResponseData:
        """
        给 Record 添加评论

        Args:
          comment: 点赞点踩类型

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/comment",
            body=maybe_transform(
                {
                    "comment": comment,
                    "group_id": group_id,
                    "record_id": record_id,
                    "dislike_reason": dislike_reason,
                    "reason_description": reason_description,
                    "reason_link": reason_link,
                },
                api_add_comment_params.APIAddCommentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseData,
        )

    def chat(
        self,
        *,
        question: str,
        app: Optional[api_chat_params.App] | NotGiven = NOT_GIVEN,
        conversation_id: str | NotGiven = NOT_GIVEN,
        debug: bool | NotGiven = NOT_GIVEN,
        files: List[str] | NotGiven = NOT_GIVEN,
        group_id: Optional[str] | NotGiven = NOT_GIVEN,
        language: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        LLM 流式对话接口

        Args:
          question: 用户输入

          app: 应用

          conversation_id: 聊天 ID

          debug: 是否调试

          files: 文件列表

          group_id: 问答组 ID

          language: 语言

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/chat",
            body=maybe_transform(
                {
                    "question": question,
                    "app": app,
                    "conversation_id": conversation_id,
                    "debug": debug,
                    "files": files,
                    "group_id": group_id,
                    "language": language,
                },
                api_chat_params.APIChatParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def get_record(
        self,
        conversation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIGetRecordResponse:
        """
        获取某个对话的所有问答对

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return self._get(
            f"/api/record/{conversation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIGetRecordResponse,
        )

    def list_users(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """查询所有用户接口"""
        return self._get(
            "/api/user",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def stop_generation(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResponseData:
        """停止生成"""
        return self._post(
            "/api/stop",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseData,
        )


class AsyncAPIResource(_resource.AsyncAPIResource):
    @cached_property
    def conversation(self) -> AsyncConversationResource:
        return AsyncConversationResource(self._client)

    @cached_property
    def auth(self) -> AsyncAuthResource:
        return AsyncAuthResource(self._client)

    @cached_property
    def app(self) -> AsyncAppResource:
        return AsyncAppResource(self._client)

    @cached_property
    def service(self) -> AsyncServiceResource:
        return AsyncServiceResource(self._client)

    @cached_property
    def blacklist(self) -> AsyncBlacklistResource:
        return AsyncBlacklistResource(self._client)

    @cached_property
    def document(self) -> AsyncDocumentResource:
        return AsyncDocumentResource(self._client)

    @cached_property
    def knowledge(self) -> AsyncKnowledgeResource:
        return AsyncKnowledgeResource(self._client)

    @cached_property
    def llm(self) -> AsyncLlmResource:
        return AsyncLlmResource(self._client)

    @cached_property
    def mcp(self) -> AsyncMcpResource:
        return AsyncMcpResource(self._client)

    @cached_property
    def flow(self) -> AsyncFlowResource:
        return AsyncFlowResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAPIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HongyuS/openHermes-Python-SDK#accessing-raw-response-data-eg-headers
        """
        return AsyncAPIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAPIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HongyuS/openHermes-Python-SDK#with_streaming_response
        """
        return AsyncAPIResourceWithStreamingResponse(self)

    async def add_comment(
        self,
        *,
        comment: CommentType,
        group_id: str,
        record_id: str,
        dislike_reason: str | NotGiven = NOT_GIVEN,
        reason_description: str | NotGiven = NOT_GIVEN,
        reason_link: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResponseData:
        """
        给 Record 添加评论

        Args:
          comment: 点赞点踩类型

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/comment",
            body=await async_maybe_transform(
                {
                    "comment": comment,
                    "group_id": group_id,
                    "record_id": record_id,
                    "dislike_reason": dislike_reason,
                    "reason_description": reason_description,
                    "reason_link": reason_link,
                },
                api_add_comment_params.APIAddCommentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseData,
        )

    async def chat(
        self,
        *,
        question: str,
        app: Optional[api_chat_params.App] | NotGiven = NOT_GIVEN,
        conversation_id: str | NotGiven = NOT_GIVEN,
        debug: bool | NotGiven = NOT_GIVEN,
        files: List[str] | NotGiven = NOT_GIVEN,
        group_id: Optional[str] | NotGiven = NOT_GIVEN,
        language: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        LLM 流式对话接口

        Args:
          question: 用户输入

          app: 应用

          conversation_id: 聊天 ID

          debug: 是否调试

          files: 文件列表

          group_id: 问答组 ID

          language: 语言

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/chat",
            body=await async_maybe_transform(
                {
                    "question": question,
                    "app": app,
                    "conversation_id": conversation_id,
                    "debug": debug,
                    "files": files,
                    "group_id": group_id,
                    "language": language,
                },
                api_chat_params.APIChatParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def get_record(
        self,
        conversation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIGetRecordResponse:
        """
        获取某个对话的所有问答对

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return await self._get(
            f"/api/record/{conversation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIGetRecordResponse,
        )

    async def list_users(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """查询所有用户接口"""
        return await self._get(
            "/api/user",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def stop_generation(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResponseData:
        """停止生成"""
        return await self._post(
            "/api/stop",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseData,
        )


class APIResourceWithRawResponse:
    def __init__(self, api: APIResource) -> None:
        self._api = api

        self.add_comment = to_raw_response_wrapper(
            api.add_comment,
        )
        self.chat = to_raw_response_wrapper(
            api.chat,
        )
        self.get_record = to_raw_response_wrapper(
            api.get_record,
        )
        self.list_users = to_raw_response_wrapper(
            api.list_users,
        )
        self.stop_generation = to_raw_response_wrapper(
            api.stop_generation,
        )

    @cached_property
    def conversation(self) -> ConversationResourceWithRawResponse:
        return ConversationResourceWithRawResponse(self._api.conversation)

    @cached_property
    def auth(self) -> AuthResourceWithRawResponse:
        return AuthResourceWithRawResponse(self._api.auth)

    @cached_property
    def app(self) -> AppResourceWithRawResponse:
        return AppResourceWithRawResponse(self._api.app)

    @cached_property
    def service(self) -> ServiceResourceWithRawResponse:
        return ServiceResourceWithRawResponse(self._api.service)

    @cached_property
    def blacklist(self) -> BlacklistResourceWithRawResponse:
        return BlacklistResourceWithRawResponse(self._api.blacklist)

    @cached_property
    def document(self) -> DocumentResourceWithRawResponse:
        return DocumentResourceWithRawResponse(self._api.document)

    @cached_property
    def knowledge(self) -> KnowledgeResourceWithRawResponse:
        return KnowledgeResourceWithRawResponse(self._api.knowledge)

    @cached_property
    def llm(self) -> LlmResourceWithRawResponse:
        return LlmResourceWithRawResponse(self._api.llm)

    @cached_property
    def mcp(self) -> McpResourceWithRawResponse:
        return McpResourceWithRawResponse(self._api.mcp)

    @cached_property
    def flow(self) -> FlowResourceWithRawResponse:
        return FlowResourceWithRawResponse(self._api.flow)


class AsyncAPIResourceWithRawResponse:
    def __init__(self, api: AsyncAPIResource) -> None:
        self._api = api

        self.add_comment = async_to_raw_response_wrapper(
            api.add_comment,
        )
        self.chat = async_to_raw_response_wrapper(
            api.chat,
        )
        self.get_record = async_to_raw_response_wrapper(
            api.get_record,
        )
        self.list_users = async_to_raw_response_wrapper(
            api.list_users,
        )
        self.stop_generation = async_to_raw_response_wrapper(
            api.stop_generation,
        )

    @cached_property
    def conversation(self) -> AsyncConversationResourceWithRawResponse:
        return AsyncConversationResourceWithRawResponse(self._api.conversation)

    @cached_property
    def auth(self) -> AsyncAuthResourceWithRawResponse:
        return AsyncAuthResourceWithRawResponse(self._api.auth)

    @cached_property
    def app(self) -> AsyncAppResourceWithRawResponse:
        return AsyncAppResourceWithRawResponse(self._api.app)

    @cached_property
    def service(self) -> AsyncServiceResourceWithRawResponse:
        return AsyncServiceResourceWithRawResponse(self._api.service)

    @cached_property
    def blacklist(self) -> AsyncBlacklistResourceWithRawResponse:
        return AsyncBlacklistResourceWithRawResponse(self._api.blacklist)

    @cached_property
    def document(self) -> AsyncDocumentResourceWithRawResponse:
        return AsyncDocumentResourceWithRawResponse(self._api.document)

    @cached_property
    def knowledge(self) -> AsyncKnowledgeResourceWithRawResponse:
        return AsyncKnowledgeResourceWithRawResponse(self._api.knowledge)

    @cached_property
    def llm(self) -> AsyncLlmResourceWithRawResponse:
        return AsyncLlmResourceWithRawResponse(self._api.llm)

    @cached_property
    def mcp(self) -> AsyncMcpResourceWithRawResponse:
        return AsyncMcpResourceWithRawResponse(self._api.mcp)

    @cached_property
    def flow(self) -> AsyncFlowResourceWithRawResponse:
        return AsyncFlowResourceWithRawResponse(self._api.flow)


class APIResourceWithStreamingResponse:
    def __init__(self, api: APIResource) -> None:
        self._api = api

        self.add_comment = to_streamed_response_wrapper(
            api.add_comment,
        )
        self.chat = to_streamed_response_wrapper(
            api.chat,
        )
        self.get_record = to_streamed_response_wrapper(
            api.get_record,
        )
        self.list_users = to_streamed_response_wrapper(
            api.list_users,
        )
        self.stop_generation = to_streamed_response_wrapper(
            api.stop_generation,
        )

    @cached_property
    def conversation(self) -> ConversationResourceWithStreamingResponse:
        return ConversationResourceWithStreamingResponse(self._api.conversation)

    @cached_property
    def auth(self) -> AuthResourceWithStreamingResponse:
        return AuthResourceWithStreamingResponse(self._api.auth)

    @cached_property
    def app(self) -> AppResourceWithStreamingResponse:
        return AppResourceWithStreamingResponse(self._api.app)

    @cached_property
    def service(self) -> ServiceResourceWithStreamingResponse:
        return ServiceResourceWithStreamingResponse(self._api.service)

    @cached_property
    def blacklist(self) -> BlacklistResourceWithStreamingResponse:
        return BlacklistResourceWithStreamingResponse(self._api.blacklist)

    @cached_property
    def document(self) -> DocumentResourceWithStreamingResponse:
        return DocumentResourceWithStreamingResponse(self._api.document)

    @cached_property
    def knowledge(self) -> KnowledgeResourceWithStreamingResponse:
        return KnowledgeResourceWithStreamingResponse(self._api.knowledge)

    @cached_property
    def llm(self) -> LlmResourceWithStreamingResponse:
        return LlmResourceWithStreamingResponse(self._api.llm)

    @cached_property
    def mcp(self) -> McpResourceWithStreamingResponse:
        return McpResourceWithStreamingResponse(self._api.mcp)

    @cached_property
    def flow(self) -> FlowResourceWithStreamingResponse:
        return FlowResourceWithStreamingResponse(self._api.flow)


class AsyncAPIResourceWithStreamingResponse:
    def __init__(self, api: AsyncAPIResource) -> None:
        self._api = api

        self.add_comment = async_to_streamed_response_wrapper(
            api.add_comment,
        )
        self.chat = async_to_streamed_response_wrapper(
            api.chat,
        )
        self.get_record = async_to_streamed_response_wrapper(
            api.get_record,
        )
        self.list_users = async_to_streamed_response_wrapper(
            api.list_users,
        )
        self.stop_generation = async_to_streamed_response_wrapper(
            api.stop_generation,
        )

    @cached_property
    def conversation(self) -> AsyncConversationResourceWithStreamingResponse:
        return AsyncConversationResourceWithStreamingResponse(self._api.conversation)

    @cached_property
    def auth(self) -> AsyncAuthResourceWithStreamingResponse:
        return AsyncAuthResourceWithStreamingResponse(self._api.auth)

    @cached_property
    def app(self) -> AsyncAppResourceWithStreamingResponse:
        return AsyncAppResourceWithStreamingResponse(self._api.app)

    @cached_property
    def service(self) -> AsyncServiceResourceWithStreamingResponse:
        return AsyncServiceResourceWithStreamingResponse(self._api.service)

    @cached_property
    def blacklist(self) -> AsyncBlacklistResourceWithStreamingResponse:
        return AsyncBlacklistResourceWithStreamingResponse(self._api.blacklist)

    @cached_property
    def document(self) -> AsyncDocumentResourceWithStreamingResponse:
        return AsyncDocumentResourceWithStreamingResponse(self._api.document)

    @cached_property
    def knowledge(self) -> AsyncKnowledgeResourceWithStreamingResponse:
        return AsyncKnowledgeResourceWithStreamingResponse(self._api.knowledge)

    @cached_property
    def llm(self) -> AsyncLlmResourceWithStreamingResponse:
        return AsyncLlmResourceWithStreamingResponse(self._api.llm)

    @cached_property
    def mcp(self) -> AsyncMcpResourceWithStreamingResponse:
        return AsyncMcpResourceWithStreamingResponse(self._api.mcp)

    @cached_property
    def flow(self) -> AsyncFlowResourceWithStreamingResponse:
        return AsyncFlowResourceWithStreamingResponse(self._api.flow)
