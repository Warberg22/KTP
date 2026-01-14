from typing import Dict, List, Any

Rule = Dict[str, Any]

RULES: List[Rule] = [
    # Phase 1: Symptoms -> Cause (Diagnosis)

    #400 Bad Request
    {
        "name": "Cause_BadRequest_400_Generic",
        "if": {"status_code": 400},
        "then": {
            "category": "validation",
            "cause": "bad_request_generic",
            "diagnosis": "Bad request (client error).",
        },
    },
    {
        "name": "Cause_InvalidJson_400",
        "if": {"status_code": 400, "error_keyword": "json"},
        "then": {
            "category": "validation",
            "cause": "invalid_json",
            "diagnosis": "Invalid JSON body.",
        },
    },
    {
        "name": "Cause_MissingField_400",
        "if": {"status_code": 400, "error_keyword": "missing_field"},
        "then": {
            "category": "validation",
            "cause": "missing_required_field",
            "diagnosis": "Missing required field in request.",
        },
    },
    {
        "name": "Cause_InvalidType_400",
        "if": {"status_code": 400, "error_keyword": "type"},
        "then": {
            "category": "validation",
            "cause": "invalid_data_type",
            "diagnosis": "Invalid data type in request payload.",
        },
    },
    {
        "name": "Cause_ValidationFailed_400",
        "if": {"status_code": 400, "error_keyword": "validation"},
        "then": {
            "category": "validation",
            "cause": "validation_failed",
            "diagnosis": "Request validation failed.",
        },
    },
    {
        "name": "Cause_EmptyBody_400",
        "if": {"status_code": 400, "error_keyword": "empty"},
        "then": {
            "category": "validation",
            "cause": "empty_body",
            "diagnosis": "Empty request body.",
        },
    },
    {
        "name": "Cause_PayloadTooLarge_400",
        "if": {"status_code": 400, "error_keyword": "size"},
        "then": {
            "category": "validation",
            "cause": "payload_too_large",
            "diagnosis": "Request payload too large.",
        },
    },
    {
        "name": "Cause_MalformedQuery_400",
        "if": {"status_code": 400, "error_keyword": "query"},
        "then": {
            "category": "validation",
            "cause": "malformed_query",
            "diagnosis": "Malformed query parameters.",
        },
    },

    #401 Unauthorized (Authentication)
    {
        "name": "Cause_Unauthorized_401_Generic",
        "if": {"status_code": 401},
        "then": {
            "category": "auth",
            "cause": "unauthorized_generic",
            "diagnosis": "Unauthorized request (authentication problem).",
        },
    },
    {
        "name": "Cause_MissingAuthHeader_401",
        "if": {"status_code": 401, "has_auth_header": "no"},
        "then": {
            "category": "auth",
            "cause": "missing_auth_header",
            "diagnosis": "Missing authentication header.",
        },
    },
    {
        "name": "Cause_InvalidCredentials_401",
        "if": {"status_code": 401, "has_auth_header": "yes"},
        "then": {
            "category": "auth",
            "cause": "invalid_or_expired_credentials",
            "diagnosis": "Invalid or expired authentication credentials.",
        },
    },
    {
        "name": "Cause_ExpiredToken_401",
        "if": {"status_code": 401, "error_keyword": "expired"},
        "then": {
            "category": "auth",
            "cause": "expired_token",
            "diagnosis": "Expired authentication token.",
        },
    },
    {
        "name": "Cause_MalformedToken_401",
        "if": {"status_code": 401, "error_keyword": "malformed"},
        "then": {
            "category": "auth",
            "cause": "malformed_token",
            "diagnosis": "Malformed authentication token.",
        },
    },
    {
        "name": "Cause_TokenSignatureInvalid_401",
        "if": {"status_code": 401, "error_keyword": "signature"},
        "then": {
            "category": "auth",
            "cause": "invalid_token_signature",
            "diagnosis": "Invalid token signature.",
        },
    },
    {
        "name": "Cause_TokenRevoked_401",
        "if": {"status_code": 401, "error_keyword": "revoked"},
        "then": {
            "category": "auth",
            "cause": "revoked_token",
            "diagnosis": "Authentication token has been revoked.",
        },
    },
    {
        "name": "Cause_MissingApiKey_401",
        "if": {"status_code": 401, "error_keyword": "api_key"},
        "then": {
            "category": "auth",
            "cause": "missing_api_key",
            "diagnosis": "Missing API key.",
        },
    },
    {
        "name": "Cause_WrongAuthScheme_401",
        "if": {"status_code": 401, "error_keyword": "scheme"},
        "then": {
            "category": "auth",
            "cause": "wrong_auth_scheme",
            "diagnosis": "Incorrect authentication scheme.",
        },
    },

    #403 Forbidden (Authorization)
    {
        "name": "Cause_Forbidden_403_Generic",
        "if": {"status_code": 403},
        "then": {
            "category": "authorization",
            "cause": "forbidden_generic",
            "diagnosis": "Forbidden request (authorization problem).",
        },
    },
    {
        "name": "Cause_MissingRole_403",
        "if": {"status_code": 403, "error_keyword": "role"},
        "then": {
            "category": "authorization",
            "cause": "missing_role",
            "diagnosis": "Missing required role or permission.",
        },
    },
    {
        "name": "Cause_ScopeNotAllowed_403",
        "if": {"status_code": 403, "error_keyword": "scope"},
        "then": {
            "category": "authorization",
            "cause": "scope_not_allowed",
            "diagnosis": "Insufficient authorization scope.",
        },
    },
    {
        "name": "Cause_AccessPolicyDenied_403",
        "if": {"status_code": 403, "error_keyword": "policy"},
        "then": {
            "category": "authorization",
            "cause": "policy_denied",
            "diagnosis": "Access denied by policy.",
        },
    },
    {
        "name": "Cause_InternalEndpointForbidden_403",
        "if": {"status_code": 403, "client_type": "public_api"},
        "then": {
            "category": "authorization",
            "cause": "internal_endpoint_forbidden",
            "diagnosis": "Attempt to access internal endpoint.",
        },
    },
    {
        "name": "Cause_IpBlocked_403",
        "if": {"status_code": 403, "error_keyword": "ip"},
        "then": {
            "category": "authorization",
            "cause": "ip_blocked",
            "diagnosis": "Client IP address is blocked.",
        },
    },

    #404 Not Found (Routing)
    {
        "name": "Cause_NotFound_404_Generic",
        "if": {"status_code": 404},
        "then": {
            "category": "routing",
            "cause": "not_found_generic",
            "diagnosis": "Endpoint not found (wrong path or route).",
        },
    },
    {
        "name": "Cause_WrongApiVersion_404",
        "if": {"status_code": 404, "error_keyword": "version"},
        "then": {
            "category": "routing",
            "cause": "wrong_api_version",
            "diagnosis": "Incorrect API version in request path.",
        },
    },
    {
        "name": "Cause_ResourceNotFound_404",
        "if": {"status_code": 404, "error_keyword": "resource"},
        "then": {
            "category": "routing",
            "cause": "resource_not_found",
            "diagnosis": "Requested resource does not exist.",
        },
    },
    {
        "name": "Cause_TrailingSlashIssue_404",
        "if": {"status_code": 404, "error_keyword": "slash"},
        "then": {
            "category": "routing",
            "cause": "trailing_slash_issue",
            "diagnosis": "Incorrect trailing slash in endpoint URL.",
        },
    },
    {
        "name": "Cause_DeprecatedEndpoint_404",
        "if": {"status_code": 404, "error_keyword": "deprecated"},
        "then": {
            "category": "routing",
            "cause": "deprecated_endpoint",
            "diagnosis": "Deprecated endpoint.",
        },
    },

    #405 Method Not Allowed
    {
        "name": "Cause_WrongMethod_405",
        "if": {"status_code": 405},
        "then": {
            "category": "routing",
            "cause": "method_not_allowed",
            "diagnosis": "Method not allowed for this endpoint.",
        },
    },

    #415 Unsupported Media Type
    {
        "name": "Cause_UnsupportedMediaType_415",
        "if": {"status_code": 415},
        "then": {
            "category": "validation",
            "cause": "unsupported_media_type",
            "diagnosis": "Unsupported media type.",
        },
    },

    #429 Too Many Requests
    {
        "name": "Cause_TooManyRequests_429_Generic",
        "if": {"status_code": 429},
        "then": {
            "category": "rate_limit",
            "cause": "rate_limited_generic",
            "diagnosis": "Rate limit exceeded.",
        },
    },
    {
        "name": "Cause_PublicApiRateLimit_429",
        "if": {"status_code": 429, "client_type": "public_api"},
        "then": {
            "category": "rate_limit",
            "cause": "public_api_rate_limit",
            "diagnosis": "Public API rate limit exceeded.",
        },
    },

    #500 Internal Server Error
    {
        "name": "Cause_ServerError_500_Generic",
        "if": {"status_code": 500},
        "then": {
            "category": "server",
            "cause": "server_error_generic",
            "diagnosis": "Internal server error (unexpected failure in backend).",
        },
    },
    {
        "name": "Cause_NullPointer_500",
        "if": {"status_code": 500, "error_keyword": "null"},
        "then": {
            "category": "server",
            "cause": "null_reference",
            "diagnosis": "Unhandled null reference in backend.",
        },
    },
    {
        "name": "Cause_ConfigError_500",
        "if": {"status_code": 500, "error_keyword": "config"},
        "then": {
            "category": "server",
            "cause": "config_error",
            "diagnosis": "Backend configuration error.",
        },
    },
    {
        "name": "Cause_BackendTimeout_500",
        "if": {"status_code": 500, "error_keyword": "timeout"},
        "then": {
            "category": "server",
            "cause": "backend_timeout",
            "diagnosis": "Backend service timeout.",
        },
    },
    {
        "name": "Cause_DbConnectionError_500",
        "if": {"status_code": 500, "error_keyword": "db_connection"},
        "then": {
            "category": "server",
            "cause": "db_connection_error",
            "diagnosis": "Database connection problem.",
        },
    },
    {
        "name": "Cause_OutOfMemory_500",
        "if": {"status_code": 500, "error_keyword": "memory"},
        "then": {
            "category": "server",
            "cause": "out_of_memory",
            "diagnosis": "Out-of-memory error in backend.",
        },
    },

    #502 Bad Gateway
    {
        "name": "Cause_DependencyFailure_502",
        "if": {"status_code": 502},
        "then": {
            "category": "server",
            "cause": "bad_gateway_dependency",
            "diagnosis": "Bad gateway from downstream service.",
        },
    },

    #503 Service Unavailable
    {
        "name": "Cause_ServiceUnavailable_503",
        "if": {"status_code": 503},
        "then": {
            "category": "server",
            "cause": "service_unavailable",
            "diagnosis": "Service temporarily unavailable.",
        },
    },
    {
        "name": "Cause_CircuitBreakerOpen_503",
        "if": {"status_code": 503, "error_keyword": "circuit"},
        "then": {
            "category": "server",
            "cause": "circuit_breaker_open",
            "diagnosis": "Circuit breaker open.",
        },
    },

    #504 Gateway Timeout
    {
        "name": "Cause_GatewayTimeout_504_Generic",
        "if": {"status_code": 504},
        "then": {
            "category": "server",
            "cause": "gateway_timeout",
            "diagnosis": "Gateway timeout (upstream service did not respond in time).",
        },
    },


    #405 Method Not Allowed (method matters)
    {
        "name": "Cause_MethodNotAllowed_405_Generic",
        "if": {"status_code": 405},
        "then": {
            "category": "routing",
            "cause": "method_not_allowed",
            "diagnosis": "Method not allowed for this endpoint.",
        },
    },
    {
        "name": "Cause_MethodNotAllowed_GET_405",
        "if": {"status_code": 405, "method": "GET"},
        "then": {
            "category": "routing",
            "cause": "method_not_allowed_get",
            "diagnosis": "GET is not allowed for this endpoint.",
        },
    },
    {
        "name": "Cause_MethodNotAllowed_POST_405",
        "if": {"status_code": 405, "method": "POST"},
        "then": {
            "category": "routing",
            "cause": "method_not_allowed_post",
            "diagnosis": "POST is not allowed for this endpoint.",
        },
    },
    {
        "name": "Cause_MethodNotAllowed_PUT_405",
        "if": {"status_code": 405, "method": "PUT"},
        "then": {
            "category": "routing",
            "cause": "method_not_allowed_put",
            "diagnosis": "PUT is not allowed for this endpoint.",
        },
    },
    {
        "name": "Cause_MethodNotAllowed_DELETE_405",
        "if": {"status_code": 405, "method": "DELETE"},
        "then": {
            "category": "routing",
            "cause": "method_not_allowed_delete",
            "diagnosis": "DELETE is not allowed for this endpoint.",
        },
    },
    {
        "name": "Cause_MethodNotAllowed_PATCH_405",
        "if": {"status_code": 405, "method": "PATCH"},
        "then": {
            "category": "routing",
            "cause": "method_not_allowed_patch",
            "diagnosis": "PATCH is not allowed for this endpoint.",
        },
    },

    #400 Bad Request (method sometimes matters)
    # Common pattern: GET requests should not send JSON bodies (varies by framework).
    {
        "name": "Cause_GetWithJsonBody_400",
        "if": {"status_code": 400, "method": "GET", "error_keyword": "json"},
        "then": {
            "category": "validation",
            "cause": "get_with_json_body",
            "diagnosis": "GET request contains an invalid or unexpected JSON body.",
        },
    },

    #403 Forbidden (DELETE often restricted even when GET/POST allowed)
    {
        "name": "Cause_DeleteForbidden_403",
        "if": {"status_code": 403, "method": "DELETE"},
        "then": {
            "category": "authorization",
            "cause": "delete_forbidden",
            "diagnosis": "DELETE operation is forbidden for this resource.",
        },
    },

    #404 Not Found (optional, method-aware routing exists in some APIs)
    {
        "name": "Cause_NotFoundOnWrite_404",
        "if": {"status_code": 404, "method": "POST"},
        "then": {
            "category": "routing",
            "cause": "write_endpoint_not_found",
            "diagnosis": "Write endpoint not found (incorrect route for POST).",
        },
    },

    # Phase 2: Recommendation

    # Validation / 400
    {
        "name": "Reco_BadRequest_Generic",
        "if": {"cause": "bad_request_generic"},
        "then": {"recommendation": "Check the request body, query parameters, and required fields."},
    },
    {
        "name": "Reco_InvalidJson",
        "if": {"cause": "invalid_json"},
        "then": {"recommendation": "Validate JSON syntax and ensure the payload matches the API schema."},
    },
    {
        "name": "Reco_MissingRequiredField",
        "if": {"cause": "missing_required_field"},
        "then": {"recommendation": "Check the API documentation for required fields and include them."},
    },
    {
        "name": "Reco_InvalidDataType",
        "if": {"cause": "invalid_data_type"},
        "then": {"recommendation": "Verify field types match the API schema (e.g. string vs number)."},
    },
    {
        "name": "Reco_ValidationFailed",
        "if": {"cause": "validation_failed"},
        "then": {"recommendation": "Check validation rules and constraints defined by the API."},
    },
    {
        "name": "Reco_EmptyBody",
        "if": {"cause": "empty_body"},
        "then": {"recommendation": "Ensure the request body is not empty and contains required data."},
    },
    {
        "name": "Reco_PayloadTooLarge",
        "if": {"cause": "payload_too_large"},
        "then": {"recommendation": "Reduce payload size or split the request into smaller chunks."},
    },
    {
        "name": "Reco_MalformedQuery",
        "if": {"cause": "malformed_query"},
        "then": {"recommendation": "Verify query parameter names, values, and encoding."},
    },
    {
        "name": "Reco_UnsupportedMediaType",
        "if": {"cause": "unsupported_media_type"},
        "then": {"recommendation": "Set the Content-Type header to a format supported by the API."},
    },

    #Authentication / 401
    {
        "name": "Reco_Unauthorized_Generic",
        "if": {"cause": "unauthorized_generic"},
        "then": {"recommendation": "Verify that the request includes valid authentication credentials."},
    },
    {
        "name": "Reco_MissingAuthHeader",
        "if": {"cause": "missing_auth_header"},
        "then": {"recommendation": "Include a valid Authorization header in the request."},
    },
    {
        "name": "Reco_InvalidOrExpiredCredentials",
        "if": {"cause": "invalid_or_expired_credentials"},
        "then": {"recommendation": "Verify token validity, expiration time, and authentication configuration."},
    },
    {
        "name": "Reco_ExpiredToken",
        "if": {"cause": "expired_token"},
        "then": {"recommendation": "Refresh the token or log in again to obtain a new one."},
    },
    {
        "name": "Reco_MalformedToken",
        "if": {"cause": "malformed_token"},
        "then": {"recommendation": "Check token format and ensure it follows the expected structure."},
    },
    {
        "name": "Reco_InvalidTokenSignature",
        "if": {"cause": "invalid_token_signature"},
        "then": {"recommendation": "Verify token signing key and authentication configuration."},
    },
    {
        "name": "Reco_RevokedToken",
        "if": {"cause": "revoked_token"},
        "then": {"recommendation": "Generate a new token and ensure it is still active."},
    },
    {
        "name": "Reco_MissingApiKey",
        "if": {"cause": "missing_api_key"},
        "then": {"recommendation": "Include a valid API key in the request headers."},
    },
    {
        "name": "Reco_WrongAuthScheme",
        "if": {"cause": "wrong_auth_scheme"},
        "then": {"recommendation": "Ensure the Authorization header uses the correct scheme (e.g. Bearer)."},
    },

    #Authorization / 403
    {
        "name": "Reco_Forbidden_Generic",
        "if": {"cause": "forbidden_generic"},
        "then": {"recommendation": "Check user or service permissions and access control rules."},
    },
    {
        "name": "Reco_MissingRole",
        "if": {"cause": "missing_role"},
        "then": {"recommendation": "Assign the required role or permission to the user or service."},
    },
    {
        "name": "Reco_ScopeNotAllowed",
        "if": {"cause": "scope_not_allowed"},
        "then": {"recommendation": "Request a token with the necessary scopes."},
    },
    {
        "name": "Reco_PolicyDenied",
        "if": {"cause": "policy_denied"},
        "then": {"recommendation": "Review access policies and security rules for this endpoint."},
    },
    {
        "name": "Reco_InternalEndpointForbidden",
        "if": {"cause": "internal_endpoint_forbidden"},
        "then": {"recommendation": "Use the correct public endpoint or call the API from an internal service."},
    },
    {
        "name": "Reco_IpBlocked",
        "if": {"cause": "ip_blocked"},
        "then": {"recommendation": "Check firewall rules or IP allowlists."},
    },

    #Routing / 404 & 405
    {
        "name": "Reco_NotFound_Generic",
        "if": {"cause": "not_found_generic"},
        "then": {"recommendation": "Check the request path, API version, and routing configuration."},
    },
    {
        "name": "Reco_WrongApiVersion",
        "if": {"cause": "wrong_api_version"},
        "then": {"recommendation": "Verify the API version used in the URL."},
    },
    {
        "name": "Reco_ResourceNotFound",
        "if": {"cause": "resource_not_found"},
        "then": {"recommendation": "Verify resource identifiers and existence."},
    },
    {
        "name": "Reco_TrailingSlashIssue",
        "if": {"cause": "trailing_slash_issue"},
        "then": {"recommendation": "Check whether the endpoint requires or forbids a trailing slash."},
    },
    {
        "name": "Reco_DeprecatedEndpoint",
        "if": {"cause": "deprecated_endpoint"},
        "then": {"recommendation": "Update the client to use the latest supported endpoint."},
    },
    {
        "name": "Reco_MethodNotAllowed",
        "if": {"cause": "method_not_allowed"},
        "then": {"recommendation": "Check which HTTP methods are supported and adjust the request."},
    },

    #Rate limiting / 429
    {
        "name": "Reco_RateLimited_Generic",
        "if": {"cause": "rate_limited_generic"},
        "then": {"recommendation": "Reduce request frequency or implement exponential backoff."},
    },
    {
        "name": "Reco_PublicApiRateLimit",
        "if": {"cause": "public_api_rate_limit"},
        "then": {"recommendation": "Add client-side rate limiting and consider using API keys with higher quotas."},
    },

    #Server / 500+
    {
        "name": "Reco_ServerError_Generic",
        "if": {"cause": "server_error_generic"},
        "then": {"recommendation": "Inspect backend logs and recent code changes for unhandled errors."},
    },
    {
        "name": "Reco_NullReference",
        "if": {"cause": "null_reference"},
        "then": {"recommendation": "Inspect backend code for missing null checks."},
    },
    {
        "name": "Reco_ConfigError",
        "if": {"cause": "config_error"},
        "then": {"recommendation": "Verify environment variables and configuration files."},
    },
    {
        "name": "Reco_BackendTimeout",
        "if": {"cause": "backend_timeout"},
        "then": {"recommendation": "Check downstream service latency and increase timeout limits if needed."},
    },
    {
        "name": "Reco_DbConnectionError",
        "if": {"cause": "db_connection_error"},
        "then": {"recommendation": "Verify database availability, connection strings, and network access."},
    },
    {
        "name": "Reco_OutOfMemory",
        "if": {"cause": "out_of_memory"},
        "then": {"recommendation": "Check memory usage and adjust resource limits."},
    },
    {
        "name": "Reco_BadGatewayDependency",
        "if": {"cause": "bad_gateway_dependency"},
        "then": {"recommendation": "Check availability and health of dependent services."},
    },
    {
        "name": "Reco_ServiceUnavailable",
        "if": {"cause": "service_unavailable"},
        "then": {"recommendation": "Retry later or check service health and scaling."},
    },
    {
        "name": "Reco_CircuitBreakerOpen",
        "if": {"cause": "circuit_breaker_open"},
        "then": {"recommendation": "Allow time for recovery or investigate downstream failures."},
    },
    {
        "name": "Reco_GatewayTimeout",
        "if": {"cause": "gateway_timeout"},
        "then": {"recommendation": "Check downstream service availability and timeout settings."},
    },


    #Recommendations for 405
    {
        "name": "Reco_MethodNotAllowed_Generic",
        "if": {"cause": "method_not_allowed"},
        "then": {
            "recommendation": "Check which HTTP methods are supported by this endpoint and update the client request accordingly."
        },
    },
    {
        "name": "Reco_MethodNotAllowed_GET",
        "if": {"cause": "method_not_allowed_get"},
        "then": {
            "recommendation": "Replace GET with the method specified by the API for this endpoint (commonly POST or PUT)."
        },
    },
    {
        "name": "Reco_MethodNotAllowed_POST",
        "if": {"cause": "method_not_allowed_post"},
        "then": {
            "recommendation": "Replace POST with the correct method for this endpoint (commonly GET for retrieval or PUT/PATCH for updates)."
        },
    },
    {
        "name": "Reco_MethodNotAllowed_PUT",
        "if": {"cause": "method_not_allowed_put"},
        "then": {
            "recommendation": "Use the update method supported by this endpoint (often PATCH or POST), based on documentation."
        },
    },
    {
        "name": "Reco_MethodNotAllowed_DELETE",
        "if": {"cause": "method_not_allowed_delete"},
        "then": {
            "recommendation": "Verify whether deletion is supported. If it is, use the correct endpoint and ensure permissions allow DELETE."
        },
    },
    {
        "name": "Reco_MethodNotAllowed_PATCH",
        "if": {"cause": "method_not_allowed_patch"},
        "then": {
            "recommendation": "If partial updates are not supported, use PUT (full update) or the method specified in the API docs."
        },
    },

    #Recommendation for GET with JSON body
    {
        "name": "Reco_GetWithJsonBody_400",
        "if": {"cause": "get_with_json_body"},
        "then": {
            "recommendation": "Avoid sending a JSON body with GET. Move data to query parameters or use POST if a body is required."
        },
    },

    #Recommendation for DELETE forbidden
    {
        "name": "Reco_DeleteForbidden_403",
        "if": {"cause": "delete_forbidden"},
        "then": {
            "recommendation": "Check whether the user/service has delete permissions and whether the resource is allowed to be deleted."
        },
    },

    #Recommendation for POST 404 write endpoint not found
    {
        "name": "Reco_WriteEndpointNotFound_404",
        "if": {"cause": "write_endpoint_not_found"},
        "then": {
            "recommendation": "Verify you are using the correct POST endpoint (path and API version). Some APIs use a different path for create actions."
        },
    },

]
