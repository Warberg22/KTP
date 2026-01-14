# main.py
from typing import Dict, Any

import streamlit as st

from kb import RULES
from engine import forward_chain


KEYWORDS_BY_STATUS: Dict[int, list[str]] = {
    400: ["", "json", "missing_field", "type", "validation", "empty", "size", "query"],
    401: ["", "expired", "malformed", "signature", "revoked", "api_key", "scheme"],
    403: ["", "role", "scope", "policy", "ip"],
    404: ["", "version", "resource", "slash", "deprecated"],
    500: ["", "null", "config", "timeout", "db_connection", "memory"],
    503: ["", "circuit"],
}

STATUS_OPTIONS = [None, 400, 401, 403, 404, 405, 415, 429, 500, 502, 503, 504]

METHOD_RELEVANT_STATUS_CODES = {405, 400, 403, 404}
RELEVANT_METHOD_BY_STATUS_CODES: Dict[int, list[str]] = {
    400: ["", "GET"],
    403: ["", "DELETE"],
    404: ["", "POST"],
    405: ["", "GET", "POST", "PUT", "DELETE", "PATCH"],
}

def main() -> None:
    st.title("API Bug Diagnosis Assistant")

    st.subheader("1) Symptom Collection")

    status_code = st.selectbox(
        "HTTP status code",
        options=STATUS_OPTIONS,
        format_func=lambda x: "Select..." if x is None else str(x),
    )

    if status_code is None:
        st.info("Select a status code to continue.")
        return

    facts: Dict[str, Any] = {"status_code": status_code}

    if status_code == 401:
        facts["has_auth_header"] = st.selectbox(
            "Authorization header present?",
            options=["yes", "no"],
            help="Used by rules that distinguish missing auth header from invalid credentials.",
        )

    if status_code in (403, 429):
        facts["client_type"] = st.selectbox(
            "Client type",
            options=["public_api", "internal_service"],
            help="Used by rules that distinguish public API clients from internal services.",
        )

    keyword_options = KEYWORDS_BY_STATUS.get(status_code, [""])
    error_keyword = st.selectbox(
        "Main error keyword (optional)",
        options=keyword_options,
        help="A simplified keyword extracted from the error message/logs.",
    )
    if error_keyword:
        facts["error_keyword"] = error_keyword

    method_options = RELEVANT_METHOD_BY_STATUS_CODES.get(status_code)
    if method_options is not None:
        method = st.selectbox(
            "HTTP method (optional)",
            options=method_options,
            help="Only shown when method-dependent rules may apply for this status code.",
        )
        if method:
            facts["method"] = method

    st.subheader("2) Reasoning")

    if st.button("Run diagnosis"):
        st.markdown("**Initial facts**")
        st.json(facts)

        final_facts, fired_rules = forward_chain(facts, RULES)

        st.markdown("**Facts after reasoning**")
        st.json(final_facts)

        st.subheader("3) Result")

        diagnosis = final_facts.get("diagnosis")
        category = final_facts.get("category")
        cause = final_facts.get("cause")
        recommendation = final_facts.get("recommendation")

        if diagnosis:
            if category:
                st.success(f"Diagnosis ({category}): {diagnosis}")
            else:
                st.success(f"Diagnosis: {diagnosis}")
        else:
            st.warning("No diagnosis could be inferred with the current information.")

        if cause:
            st.caption(f"Inferred cause: `{cause}`")

        st.subheader("Recommended Action")
        if recommendation:
            st.info(recommendation)
        else:
            st.write("No recommendation could be inferred for the inferred cause.")

        st.subheader("Explanation (Rules Fired)")
        if fired_rules:
            for name in fired_rules:
                st.write(f"- {name}")
        else:
            st.write("No rules were fired.")


if __name__ == "__main__":
    main()
