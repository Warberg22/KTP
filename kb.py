from typing import Dict, List, Any

# A rule is a dictionary with:
# name: rule name
# if: conditions (facts that must match)
# then: conclusions (facts to add/update)
Rule = Dict[str, Any]

RULES: List[Rule] = [
    # Generic rules

    {
        "name": "NotFound_404_Generic",
        "if": {"status_code": 404},
        "then": {
            "diagnosis": "Endpoint not found (wrong path or route).",
            "recommendation": "Check the request path, API version, and routing configuration.",
        },
    },
    {
        "name": "BadRequest_400_Generic",
        "if": {"status_code": 400},
        "then": {
            "diagnosis": "Bad request (client error).",
            "recommendation": "Check the request body, query parameters, and required fields.",
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
        "name": "Forbidden_403_Generic",
        "if": {"status_code": 403},
        "then": {
            "diagnosis": "Forbidden request (authorization problem).",
            "recommendation": "Check user or service permissions and access control rules.",
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
        "name": "TooManyRequests_429_Generic",
        "if": {"status_code": 429},
        "then": {
            "diagnosis": "Rate limit exceeded.",
            "recommendation": "Reduce request frequency or implement exponential backoff.",
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

    # Rules that use more information
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
        "name": "UnsupportedMediaType_415",
        "if": {"status_code": 415},
        "then": {
            "diagnosis": "Unsupported media type.",
            "recommendation": "Set the Content-Type header to a format supported by the API.",
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
        "name": "PublicApiRateLimit_429",
        "if": {"status_code": 429, "client_type": "public_api"},
        "then": {
            "diagnosis": "Public API rate limit exceeded.",
            "recommendation": "Add client-side rate limiting and consider using API keys with higher quotas.",
        },
    },
]
