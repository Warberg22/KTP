from typing import Dict, List, Any

# A rule is a dictionary with:
# name: rule name
# if: conditions (facts that must match)
# then: conclusions (facts to add/update)
Rule = Dict[str, Any]

RULES: List[Rule] = [
    {
        "name": "BadRequest_400_Generic",
        "if": {"status_code": 400},
        "then": {
            "diagnosis": "Bad request (client error).",
            "recommendation": "Check the request body, query parameters, and required fields.",
        },
    },
    {
        "name": "JsonParseError_400",
        "if": {"status_code": 400, "error_keyword": "json"},
        "then": {
            "diagnosis": "Invalid JSON body.",
            "recommendation": "Validate JSON syntax and ensure the payload matches the API schema.",
        },
    },
    {
        "name": "MissingField_400",
        "if": {"status_code": 400, "error_keyword": "missing_field"},
        "then": {
            "diagnosis": "Missing required field in request.",
            "recommendation": "Check the API documentation for required fields and include them.",
        },
    },
    {
        "name": "InvalidType_400",
        "if": {"status_code": 400, "error_keyword": "type"},
        "then": {
            "diagnosis": "Invalid data type in request payload.",
            "recommendation": "Verify field types match the API schema (e.g. string vs number).",
        },
    },
    {
        "name": "ValidationFailed_400",
        "if": {"status_code": 400, "error_keyword": "validation"},
        "then": {
            "diagnosis": "Request validation failed.",
            "recommendation": "Check validation rules and constraints defined by the API.",
        },
    },
    {
        "name": "EmptyBody_400",
        "if": {"status_code": 400, "error_keyword": "empty"},
        "then": {
            "diagnosis": "Empty request body.",
            "recommendation": "Ensure the request body is not empty and contains required data.",
        },
    },
    {
        "name": "PayloadTooLarge_400",
        "if": {"status_code": 400, "error_keyword": "size"},
        "then": {
            "diagnosis": "Request payload too large.",
            "recommendation": "Reduce payload size or split the request into smaller chunks.",
        },
    },
    {
        "name": "MalformedQuery_400",
        "if": {"status_code": 400, "error_keyword": "query"},
        "then": {
            "diagnosis": "Malformed query parameters.",
            "recommendation": "Verify query parameter names, values, and encoding.",
        },
    },




    {
        "name": "Unauthorized_401_Generic",
        "if": {"status_code": 401},
        "then": {
            "diagnosis": "Unauthorized request (authentication problem).",
            "recommendation": "Verify that the request includes valid authentication credentials.",
        },
    },
    {
        "name": "MissingAuthHeader_401",
        "if": {"status_code": 401, "has_auth_header": "no"},
        "then": {
            "diagnosis": "Missing authentication header.",
            "recommendation": "Include a valid Authorization header in the request.",
        },
    },
    {
        "name": "InvalidCredentials_401",
        "if": {"status_code": 401, "has_auth_header": "yes"},
        "then": {
            "diagnosis": "Invalid or expired authentication credentials.",
            "recommendation": "Verify token validity, expiration time, and authentication configuration.",
        },
    },
    {
        "name": "ExpiredToken_401",
        "if": {"status_code": 401, "error_keyword": "expired"},
        "then": {
            "diagnosis": "Expired authentication token.",
            "recommendation": "Refresh the token or log in again to obtain a new one.",
        },
    },
    {
        "name": "MalformedToken_401",
        "if": {"status_code": 401, "error_keyword": "malformed"},
        "then": {
            "diagnosis": "Malformed authentication token.",
            "recommendation": "Check token format and ensure it follows the expected structure.",
        },
    },
    {
        "name": "TokenSignatureInvalid_401",
        "if": {"status_code": 401, "error_keyword": "signature"},
        "then": {
            "diagnosis": "Invalid token signature.",
            "recommendation": "Verify token signing key and authentication configuration.",
        },
    },
    {
        "name": "TokenRevoked_401",
        "if": {"status_code": 401, "error_keyword": "revoked"},
        "then": {
            "diagnosis": "Authentication token has been revoked.",
            "recommendation": "Generate a new token and ensure it is still active.",
        },
    },
    {
        "name": "MissingApiKey_401",
        "if": {"status_code": 401, "error_keyword": "api_key"},
        "then": {
            "diagnosis": "Missing API key.",
            "recommendation": "Include a valid API key in the request headers.",
        },
    },
    {
        "name": "WrongAuthScheme_401",
        "if": {"status_code": 401, "error_keyword": "scheme"},
        "then": {
            "diagnosis": "Incorrect authentication scheme.",
            "recommendation": "Ensure the Authorization header uses the correct scheme (e.g. Bearer).",
        },
    },




    {
        "name": "Forbidden_403_Generic",
        "if": {"status_code": 403},
        "then": {
            "diagnosis": "Forbidden request (authorization problem).",
            "recommendation": "Check user or service permissions and access control rules.",
        },
    },
    {
        "name": "MissingRole_403",
        "if": {"status_code": 403, "error_keyword": "role"},
        "then": {
            "diagnosis": "Missing required role or permission.",
            "recommendation": "Assign the required role or permission to the user or service.",
        },
    },
    {
        "name": "ScopeNotAllowed_403",
        "if": {"status_code": 403, "error_keyword": "scope"},
        "then": {
            "diagnosis": "Insufficient authorization scope.",
            "recommendation": "Request a token with the necessary scopes.",
        },
    },
    {
        "name": "AccessPolicyDenied_403",
        "if": {"status_code": 403, "error_keyword": "policy"},
        "then": {
            "diagnosis": "Access denied by policy.",
            "recommendation": "Review access policies and security rules for this endpoint.",
        },
    },
    {
        "name": "InternalEndpointForbidden_403",
        "if": {"status_code": 403, "client_type": "public_api"},
        "then": {
            "diagnosis": "Attempt to access internal endpoint.",
            "recommendation": "Use the correct public endpoint or call the API from an internal service.",
        },
    },
    {
        "name": "IpBlocked_403",
        "if": {"status_code": 403, "error_keyword": "ip"},
        "then": {
            "diagnosis": "Client IP address is blocked.",
            "recommendation": "Check firewall rules or IP allowlists.",
        },
    },


    {
        "name": "NotFound_404_Generic",
        "if": {"status_code": 404},
        "then": {
            "diagnosis": "Endpoint not found (wrong path or route).",
            "recommendation": "Check the request path, API version, and routing configuration.",
        },
    },
    {
        "name": "WrongApiVersion_404",
        "if": {"status_code": 404, "error_keyword": "version"},
        "then": {
            "diagnosis": "Incorrect API version in request path.",
            "recommendation": "Verify the API version used in the URL.",
        },
    },
    {
        "name": "ResourceNotFound_404",
        "if": {"status_code": 404, "error_keyword": "resource"},
        "then": {
            "diagnosis": "Requested resource does not exist.",
            "recommendation": "Verify resource identifiers and existence.",
        },
    },
    {
        "name": "TrailingSlashIssue_404",
        "if": {"status_code": 404, "error_keyword": "slash"},
        "then": {
            "diagnosis": "Incorrect trailing slash in endpoint URL.",
            "recommendation": "Check whether the endpoint requires or forbids a trailing slash.",
        },
    },
    {
        "name": "DeprecatedEndpoint_404",
        "if": {"status_code": 404, "error_keyword": "deprecated"},
        "then": {
            "diagnosis": "Deprecated endpoint.",
            "recommendation": "Update the client to use the latest supported endpoint.",
        },
    },



    {
        "name": "WrongMethod_405",
        "if": {"status_code": 405},
        "then": {
            "diagnosis": "Method not allowed for this endpoint.",
            "recommendation": "Check which HTTP methods are supported and adjust the request.",
        },
    },


    {
        "name": "TooManyRequests_429_Generic",
        "if": {"status_code": 429},
        "then": {
            "diagnosis": "Rate limit exceeded.",
            "recommendation": "Reduce request frequency or implement exponential backoff.",
        },
    },
    {
        "name": "UnsupportedMediaType_415",
        "if": {"status_code": 415},
        "then": {
            "diagnosis": "Unsupported media type.",
            "recommendation": "Set the Content-Type header to a format supported by the API.",
        },
    },
    {
        "name": "PublicApiRateLimit_429",
        "if": {"status_code": 429, "client_type": "public_api"},
        "then": {
            "diagnosis": "Public API rate limit exceeded.",
            "recommendation": "Add client-side rate limiting and consider using API keys with higher quotas.",
        },
    },

    {
        "name": "ServerError_500_Generic",
        "if": {"status_code": 500},
        "then": {
            "diagnosis": "Internal server error (unexpected failure in backend).",
            "recommendation": "Inspect backend logs and recent code changes for unhandled errors.",
        },
    },
    {
        "name": "NullPointer_500",
        "if": {"status_code": 500, "error_keyword": "null"},
        "then": {
            "diagnosis": "Unhandled null reference in backend.",
            "recommendation": "Inspect backend code for missing null checks.",
        },
    },
    {
        "name": "ConfigError_500",
        "if": {"status_code": 500, "error_keyword": "config"},
        "then": {
            "diagnosis": "Backend configuration error.",
            "recommendation": "Verify environment variables and configuration files.",
        },
    },
    {
        "name": "BackendTimeout_500",
        "if": {"status_code": 500, "error_keyword": "timeout"},
        "then": {
            "diagnosis": "Backend service timeout.",
            "recommendation": "Check downstream service latency and increase timeout limits if needed.",
        },
    },
    {
        "name": "DbConnectionError_500",
        "if": {"status_code": 500, "error_keyword": "db_connection"},
        "then": {
            "diagnosis": "Database connection problem.",
            "recommendation": "Verify database availability, connection strings, and network access.",
        },
    },
    {
        "name": "DependencyFailure_502",
        "if": {"status_code": 502},
        "then": {
            "diagnosis": "Bad gateway from downstream service.",
            "recommendation": "Check availability and health of dependent services.",
        },
    },
    {
        "name": "ServiceUnavailable_503",
        "if": {"status_code": 503},
        "then": {
            "diagnosis": "Service temporarily unavailable.",
            "recommendation": "Retry later or check service health and scaling.",
        },
    },
    {
        "name": "CircuitBreakerOpen_503",
        "if": {"status_code": 503, "error_keyword": "circuit"},
        "then": {
            "diagnosis": "Circuit breaker open.",
            "recommendation": "Allow time for recovery or investigate downstream failures.",
        },
    },
    {
        "name": "OutOfMemory_500",
        "if": {"status_code": 500, "error_keyword": "memory"},
        "then": {
            "diagnosis": "Out-of-memory error in backend.",
            "recommendation": "Check memory usage and adjust resource limits.",
        },
    },
    {
        "name": "GatewayTimeout_504_Generic",
        "if": {"status_code": 504},
        "then": {
            "diagnosis": "Gateway timeout (upstream service did not respond in time).",
            "recommendation": "Check downstream service availability and timeout settings.",
        },
    },
]
