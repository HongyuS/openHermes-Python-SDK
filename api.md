# API

Types:

```python
from openhermes.types import CommentType, APIGetRecordResponse
```

Methods:

- <code title="post /api/comment">client.api.<a href="./src/openhermes/resources/api/api.py">add_comment</a>(\*\*<a href="src/openhermes/types/api_add_comment_params.py">params</a>) -> <a href="./src/openhermes/types/api/response_data.py">ResponseData</a></code>
- <code title="post /api/chat">client.api.<a href="./src/openhermes/resources/api/api.py">chat</a>(\*\*<a href="src/openhermes/types/api_chat_params.py">params</a>) -> object</code>
- <code title="get /api/record/{conversation_id}">client.api.<a href="./src/openhermes/resources/api/api.py">get_record</a>(conversation_id) -> <a href="./src/openhermes/types/api_get_record_response.py">APIGetRecordResponse</a></code>
- <code title="get /api/user">client.api.<a href="./src/openhermes/resources/api/api.py">list_users</a>() -> object</code>
- <code title="post /api/stop">client.api.<a href="./src/openhermes/resources/api/api.py">stop_generation</a>() -> <a href="./src/openhermes/types/api/response_data.py">ResponseData</a></code>

## Conversation

Types:

```python
from openhermes.types.api import (
    ConversationListItem,
    ResponseData,
    ConversationCreateResponse,
    ConversationUpdateResponse,
    ConversationListResponse,
)
```

Methods:

- <code title="post /api/conversation">client.api.conversation.<a href="./src/openhermes/resources/api/conversation.py">create</a>(\*\*<a href="src/openhermes/types/api/conversation_create_params.py">params</a>) -> <a href="./src/openhermes/types/api/conversation_create_response.py">ConversationCreateResponse</a></code>
- <code title="put /api/conversation">client.api.conversation.<a href="./src/openhermes/resources/api/conversation.py">update</a>(\*\*<a href="src/openhermes/types/api/conversation_update_params.py">params</a>) -> <a href="./src/openhermes/types/api/conversation_update_response.py">ConversationUpdateResponse</a></code>
- <code title="get /api/conversation">client.api.conversation.<a href="./src/openhermes/resources/api/conversation.py">list</a>() -> <a href="./src/openhermes/types/api/conversation_list_response.py">ConversationListResponse</a></code>
- <code title="delete /api/conversation">client.api.conversation.<a href="./src/openhermes/resources/api/conversation.py">delete</a>(\*\*<a href="src/openhermes/types/api/conversation_delete_params.py">params</a>) -> <a href="./src/openhermes/types/api/response_data.py">ResponseData</a></code>

## Auth

Types:

```python
from openhermes.types.api import AuthUser, AuthRedirectResponse
```

Methods:

- <code title="get /api/auth/login">client.api.auth.<a href="./src/openhermes/resources/api/auth/auth.py">login</a>(\*\*<a href="src/openhermes/types/api/auth_login_params.py">params</a>) -> object</code>
- <code title="get /api/auth/redirect">client.api.auth.<a href="./src/openhermes/resources/api/auth/auth.py">redirect</a>() -> <a href="./src/openhermes/types/api/auth_redirect_response.py">AuthRedirectResponse</a></code>
- <code title="get /api/auth/user">client.api.auth.<a href="./src/openhermes/resources/api/auth/auth.py">retrieve_user</a>() -> <a href="./src/openhermes/types/api/auth_user.py">AuthUser</a></code>
- <code title="post /api/auth/update_revision_number">client.api.auth.<a href="./src/openhermes/resources/api/auth/auth.py">update_revision</a>() -> <a href="./src/openhermes/types/api/auth_user.py">AuthUser</a></code>

### Logout

Methods:

- <code title="get /api/auth/logout">client.api.auth.logout.<a href="./src/openhermes/resources/api/auth/logout.py">get</a>() -> <a href="./src/openhermes/types/api/response_data.py">ResponseData</a></code>
- <code title="post /api/auth/logout">client.api.auth.logout.<a href="./src/openhermes/resources/api/auth/logout.py">post</a>(\*\*<a href="src/openhermes/types/api/auth/logout_post_params.py">params</a>) -> <a href="./src/openhermes/types/api/response_data.py">ResponseData</a></code>

### Key

Types:

```python
from openhermes.types.api.auth import KeyCheckResponse, KeyManageResponse
```

Methods:

- <code title="get /api/auth/key">client.api.auth.key.<a href="./src/openhermes/resources/api/auth/key.py">check</a>() -> <a href="./src/openhermes/types/api/auth/key_check_response.py">KeyCheckResponse</a></code>
- <code title="post /api/auth/key">client.api.auth.key.<a href="./src/openhermes/resources/api/auth/key.py">manage</a>(\*\*<a href="src/openhermes/types/api/auth/key_manage_params.py">params</a>) -> <a href="./src/openhermes/types/api/auth/key_manage_response.py">KeyManageResponse</a></code>

## App

Types:

```python
from openhermes.types.api import (
    AppFlowInfo,
    AppLink,
    AppPermissionData,
    AppType,
    BaseAppOperation,
    AppRetrieveResponse,
    AppListResponse,
    AppDeleteResponse,
    AppCreateOrUpdateResponse,
    AppListRecentResponse,
    AppModifyFavoriteResponse,
)
```

Methods:

- <code title="get /api/app/{appId}">client.api.app.<a href="./src/openhermes/resources/api/app.py">retrieve</a>(app_id) -> <a href="./src/openhermes/types/api/app_retrieve_response.py">AppRetrieveResponse</a></code>
- <code title="get /api/app">client.api.app.<a href="./src/openhermes/resources/api/app.py">list</a>(\*\*<a href="src/openhermes/types/api/app_list_params.py">params</a>) -> <a href="./src/openhermes/types/api/app_list_response.py">AppListResponse</a></code>
- <code title="delete /api/app/{appId}">client.api.app.<a href="./src/openhermes/resources/api/app.py">delete</a>(app_id) -> <a href="./src/openhermes/types/api/app_delete_response.py">AppDeleteResponse</a></code>
- <code title="post /api/app">client.api.app.<a href="./src/openhermes/resources/api/app.py">create_or_update</a>(\*\*<a href="src/openhermes/types/api/app_create_or_update_params.py">params</a>) -> <a href="./src/openhermes/types/api/app_create_or_update_response.py">AppCreateOrUpdateResponse</a></code>
- <code title="get /api/app/recent">client.api.app.<a href="./src/openhermes/resources/api/app.py">list_recent</a>(\*\*<a href="src/openhermes/types/api/app_list_recent_params.py">params</a>) -> <a href="./src/openhermes/types/api/app_list_recent_response.py">AppListRecentResponse</a></code>
- <code title="put /api/app/{appId}">client.api.app.<a href="./src/openhermes/resources/api/app.py">modify_favorite</a>(app_id, \*\*<a href="src/openhermes/types/api/app_modify_favorite_params.py">params</a>) -> <a href="./src/openhermes/types/api/app_modify_favorite_response.py">AppModifyFavoriteResponse</a></code>
- <code title="post /api/app/{appId}">client.api.app.<a href="./src/openhermes/resources/api/app.py">publish</a>(app_id) -> <a href="./src/openhermes/types/api/base_app_operation.py">BaseAppOperation</a></code>

## Service

Types:

```python
from openhermes.types.api import (
    ServiceAPIData,
    ServiceRetrieveResponse,
    ServiceUpdateResponse,
    ServiceListResponse,
    ServiceDeleteResponse,
    ServiceModifyFavoriteResponse,
)
```

Methods:

- <code title="get /api/service/{serviceId}">client.api.service.<a href="./src/openhermes/resources/api/service.py">retrieve</a>(service_id, \*\*<a href="src/openhermes/types/api/service_retrieve_params.py">params</a>) -> <a href="./src/openhermes/types/api/service_retrieve_response.py">ServiceRetrieveResponse</a></code>
- <code title="post /api/service">client.api.service.<a href="./src/openhermes/resources/api/service.py">update</a>(\*\*<a href="src/openhermes/types/api/service_update_params.py">params</a>) -> <a href="./src/openhermes/types/api/service_update_response.py">ServiceUpdateResponse</a></code>
- <code title="get /api/service">client.api.service.<a href="./src/openhermes/resources/api/service.py">list</a>(\*\*<a href="src/openhermes/types/api/service_list_params.py">params</a>) -> <a href="./src/openhermes/types/api/service_list_response.py">ServiceListResponse</a></code>
- <code title="delete /api/service/{serviceId}">client.api.service.<a href="./src/openhermes/resources/api/service.py">delete</a>(service_id) -> <a href="./src/openhermes/types/api/service_delete_response.py">ServiceDeleteResponse</a></code>
- <code title="put /api/service/{serviceId}">client.api.service.<a href="./src/openhermes/resources/api/service.py">modify_favorite</a>(service_id, \*\*<a href="src/openhermes/types/api/service_modify_favorite_params.py">params</a>) -> <a href="./src/openhermes/types/api/service_modify_favorite_response.py">ServiceModifyFavoriteResponse</a></code>

## Blacklist

Methods:

- <code title="post /api/blacklist/complaint">client.api.blacklist.<a href="./src/openhermes/resources/api/blacklist/blacklist.py">report_abuse</a>(\*\*<a href="src/openhermes/types/api/blacklist_report_abuse_params.py">params</a>) -> <a href="./src/openhermes/types/api/response_data.py">ResponseData</a></code>

### User

Types:

```python
from openhermes.types.api.blacklist import UserGetResponse
```

Methods:

- <code title="post /api/blacklist/user">client.api.blacklist.user.<a href="./src/openhermes/resources/api/blacklist/user.py">change</a>(\*\*<a href="src/openhermes/types/api/blacklist/user_change_params.py">params</a>) -> <a href="./src/openhermes/types/api/response_data.py">ResponseData</a></code>
- <code title="get /api/blacklist/user">client.api.blacklist.user.<a href="./src/openhermes/resources/api/blacklist/user.py">get</a>(\*\*<a href="src/openhermes/types/api/blacklist/user_get_params.py">params</a>) -> <a href="./src/openhermes/types/api/blacklist/user_get_response.py">UserGetResponse</a></code>

### Question

Types:

```python
from openhermes.types.api.blacklist import GetBlacklistQuestion
```

Methods:

- <code title="post /api/blacklist/question">client.api.blacklist.question.<a href="./src/openhermes/resources/api/blacklist/question.py">change</a>(\*\*<a href="src/openhermes/types/api/blacklist/question_change_params.py">params</a>) -> <a href="./src/openhermes/types/api/response_data.py">ResponseData</a></code>
- <code title="get /api/blacklist/question">client.api.blacklist.question.<a href="./src/openhermes/resources/api/blacklist/question.py">get</a>(\*\*<a href="src/openhermes/types/api/blacklist/question_get_params.py">params</a>) -> <a href="./src/openhermes/types/api/blacklist/get_blacklist_question.py">GetBlacklistQuestion</a></code>

### Abuse

Methods:

- <code title="post /api/blacklist/abuse">client.api.blacklist.abuse.<a href="./src/openhermes/resources/api/blacklist/abuse.py">change</a>(\*\*<a href="src/openhermes/types/api/blacklist/abuse_change_params.py">params</a>) -> <a href="./src/openhermes/types/api/response_data.py">ResponseData</a></code>
- <code title="get /api/blacklist/abuse">client.api.blacklist.abuse.<a href="./src/openhermes/resources/api/blacklist/abuse.py">get</a>(\*\*<a href="src/openhermes/types/api/blacklist/abuse_get_params.py">params</a>) -> <a href="./src/openhermes/types/api/blacklist/get_blacklist_question.py">GetBlacklistQuestion</a></code>

## Document

Types:

```python
from openhermes.types.api import DocumentGetListResponse
```

Methods:

- <code title="delete /api/document/{document_id}">client.api.document.<a href="./src/openhermes/resources/api/document.py">delete</a>(document_id) -> <a href="./src/openhermes/types/api/response_data.py">ResponseData</a></code>
- <code title="get /api/document/{conversation_id}">client.api.document.<a href="./src/openhermes/resources/api/document.py">get_list</a>(conversation_id, \*\*<a href="src/openhermes/types/api/document_get_list_params.py">params</a>) -> <a href="./src/openhermes/types/api/document_get_list_response.py">DocumentGetListResponse</a></code>
- <code title="post /api/document/{conversation_id}">client.api.document.<a href="./src/openhermes/resources/api/document.py">upload</a>(conversation_id, \*\*<a href="src/openhermes/types/api/document_upload_params.py">params</a>) -> object</code>

## Knowledge

Types:

```python
from openhermes.types.api import KnowledgeListResponse
```

Methods:

- <code title="put /api/knowledge">client.api.knowledge.<a href="./src/openhermes/resources/api/knowledge.py">update</a>(\*\*<a href="src/openhermes/types/api/knowledge_update_params.py">params</a>) -> <a href="./src/openhermes/types/api/response_data.py">ResponseData</a></code>
- <code title="get /api/knowledge">client.api.knowledge.<a href="./src/openhermes/resources/api/knowledge.py">list</a>(\*\*<a href="src/openhermes/types/api/knowledge_list_params.py">params</a>) -> <a href="./src/openhermes/types/api/knowledge_list_response.py">KnowledgeListResponse</a></code>

## Llm

Types:

```python
from openhermes.types.api import LlmListResponse, LlmListProvidersResponse
```

Methods:

- <code title="get /api/llm">client.api.llm.<a href="./src/openhermes/resources/api/llm.py">list</a>(\*\*<a href="src/openhermes/types/api/llm_list_params.py">params</a>) -> <a href="./src/openhermes/types/api/llm_list_response.py">LlmListResponse</a></code>
- <code title="delete /api/llm">client.api.llm.<a href="./src/openhermes/resources/api/llm.py">delete</a>(\*\*<a href="src/openhermes/types/api/llm_delete_params.py">params</a>) -> object</code>
- <code title="put /api/llm">client.api.llm.<a href="./src/openhermes/resources/api/llm.py">create_or_update</a>(\*\*<a href="src/openhermes/types/api/llm_create_or_update_params.py">params</a>) -> object</code>
- <code title="get /api/llm/provider">client.api.llm.<a href="./src/openhermes/resources/api/llm.py">list_providers</a>() -> <a href="./src/openhermes/types/api/llm_list_providers_response.py">LlmListProvidersResponse</a></code>
- <code title="put /api/llm/conv">client.api.llm.<a href="./src/openhermes/resources/api/llm.py">update_conv</a>(\*\*<a href="src/openhermes/types/api/llm_update_conv_params.py">params</a>) -> object</code>

## Mcp

Types:

```python
from openhermes.types.api import (
    BaseMcpServiceOperation,
    McpType,
    McpDeleteResponse,
    McpActivateOrDeactivateResponse,
    McpCreateOrUpdateResponse,
    McpGetDetailResponse,
    McpGetListResponse,
)
```

Methods:

- <code title="delete /api/mcp/{serviceId}">client.api.mcp.<a href="./src/openhermes/resources/api/mcp.py">delete</a>(service_id) -> <a href="./src/openhermes/types/api/mcp_delete_response.py">McpDeleteResponse</a></code>
- <code title="post /api/mcp/{serviceId}">client.api.mcp.<a href="./src/openhermes/resources/api/mcp.py">activate_or_deactivate</a>(service_id, \*\*<a href="src/openhermes/types/api/mcp_activate_or_deactivate_params.py">params</a>) -> <a href="./src/openhermes/types/api/mcp_activate_or_deactivate_response.py">McpActivateOrDeactivateResponse</a></code>
- <code title="post /api/mcp">client.api.mcp.<a href="./src/openhermes/resources/api/mcp.py">create_or_update</a>(\*\*<a href="src/openhermes/types/api/mcp_create_or_update_params.py">params</a>) -> <a href="./src/openhermes/types/api/mcp_create_or_update_response.py">McpCreateOrUpdateResponse</a></code>
- <code title="get /api/mcp/{serviceId}">client.api.mcp.<a href="./src/openhermes/resources/api/mcp.py">get_detail</a>(service_id, \*\*<a href="src/openhermes/types/api/mcp_get_detail_params.py">params</a>) -> <a href="./src/openhermes/types/api/mcp_get_detail_response.py">McpGetDetailResponse</a></code>
- <code title="get /api/mcp">client.api.mcp.<a href="./src/openhermes/resources/api/mcp.py">get_list</a>(\*\*<a href="src/openhermes/types/api/mcp_get_list_params.py">params</a>) -> <a href="./src/openhermes/types/api/mcp_get_list_response.py">McpGetListResponse</a></code>

## Flow

Types:

```python
from openhermes.types.api import (
    EdgeItem,
    FlowItemOutput,
    NodeItem,
    PositionItem,
    FlowUpdateResponse,
    FlowDeleteResponse,
    FlowGetResponse,
    FlowGetServicesResponse,
)
```

Methods:

- <code title="put /api/flow">client.api.flow.<a href="./src/openhermes/resources/api/flow.py">update</a>(\*\*<a href="src/openhermes/types/api/flow_update_params.py">params</a>) -> <a href="./src/openhermes/types/api/flow_update_response.py">FlowUpdateResponse</a></code>
- <code title="delete /api/flow">client.api.flow.<a href="./src/openhermes/resources/api/flow.py">delete</a>(\*\*<a href="src/openhermes/types/api/flow_delete_params.py">params</a>) -> <a href="./src/openhermes/types/api/flow_delete_response.py">FlowDeleteResponse</a></code>
- <code title="get /api/flow">client.api.flow.<a href="./src/openhermes/resources/api/flow.py">get</a>(\*\*<a href="src/openhermes/types/api/flow_get_params.py">params</a>) -> <a href="./src/openhermes/types/api/flow_get_response.py">FlowGetResponse</a></code>
- <code title="get /api/flow/service">client.api.flow.<a href="./src/openhermes/resources/api/flow.py">get_services</a>() -> <a href="./src/openhermes/types/api/flow_get_services_response.py">FlowGetServicesResponse</a></code>

# HealthCheck

Types:

```python
from openhermes.types import HealthCheckCheckResponse
```

Methods:

- <code title="get /health_check">client.health_check.<a href="./src/openhermes/resources/health_check.py">check</a>() -> <a href="./src/openhermes/types/health_check_check_response.py">HealthCheckCheckResponse</a></code>
