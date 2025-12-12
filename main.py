from typing import Dict, Any

import streamlit as st

from kb import RULES
from engine import forward_chain


def main():
    st.title("API Bug Diagnosis Assistant")
    st.write(
        "This is a system draft which will be expanded later with more rules and more facts that can influence the output."
    )

    st.subheader("Request & Error Information")

    col1, col2 = st.columns(2)

    with col1:
        status_code = st.selectbox(
            "HTTP status code",
            options=[None, 400, 401, 403, 404, 415, 429, 500, 504],
            format_func=lambda x: "Select..." if x is None else str(x),
        )

        method = st.selectbox(
            "HTTP method",
            options=["GET", "POST", "PUT", "DELETE", "PATCH"],
        )

    with col2:
        has_auth_header = st.selectbox(
            "Does the request include an Authorization header?",
            options=["unknown", "yes", "no"]
        )

        client_type = st.selectbox(
            "Client type",
            options=["unknown", "public_api", "internal_service"]
        )

        error_keyword = st.selectbox(
            "Main error keyword",
            options=[
                "",
                "json",
                "missing_field",
                "type",
                "validation",
                "empty",
                "size",
                "query",
                "expired",
                "malformed",
                "signature",
                "revoked",
                "api_key",
                "scheme",
                "role",
                "scope",
                "policy",
                "ip",
                "version",
                "resource",
                "slash",
                "deprecated",
                "null",
                "config",
                "timeout",
                "db_connection",
                "circuit",
                "memory",
            ],
            index=0
        )

    if st.button("Run diagnosis"):
        facts: Dict[str, Any] = {
            "method": method,
        }

        if status_code is not None:
            facts["status_code"] = status_code

        if has_auth_header in ("yes", "no"):
            facts["has_auth_header"] = has_auth_header

        if client_type != "unknown":
            facts["client_type"] = client_type

        if error_keyword:
            facts["error_keyword"] = error_keyword

        st.subheader("Initial Facts")
        st.json(facts)

        final_facts, fired_rules = forward_chain(facts, RULES)

        st.subheader("Facts After Reasoning")
        st.json(final_facts)

        diagnosis = final_facts.get("diagnosis")
        recommendation = final_facts.get("recommendation")

        st.subheader("Diagnosis")
        if diagnosis:
            st.success(diagnosis)
        else:
            st.warning("No diagnosis could be inferred with the current information.")

        st.subheader("Recommendation")
        if recommendation:
            st.info(recommendation)
        else:
            st.write("No specific recommendation available.")

        st.subheader("Rules fired")
        if fired_rules:
            for name in fired_rules:
                st.write(f"- {name}")
        else:
            st.write("No rules were fired.")


if __name__ == "__main__":
    main()
