"""
============================================================
BusinessPulse-AI
Main Streamlit Application
============================================================
"""

# ============================================================
# Import Libraries
# ============================================================

import streamlit as st

from config import (
    PAGE_TITLE,
    PAGE_ICON,
    LAYOUT,
    APP_NAME,
    APP_SUBTITLE,
    APP_VERSION,
    MODEL_NAME,
    MODEL_ACCURACY,
    TOTAL_FEATURES,
    API_STATUS,
)
from styles import load_css
from forms import customer_form
from api_utils import predict_customer
from results_ui import display_results

# ============================================================
# Streamlit Page Configuration
# ============================================================

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT
)

# ============================================================
# Load Custom CSS
# ============================================================

load_css()
# ============================================================
# Sidebar
# ============================================================

with st.sidebar:

    st.title("📊 BusinessPulse-AI")

    st.markdown("---")

    st.subheader("Project Information")

    st.write(f"**Model:** {MODEL_NAME}")

    st.write("**Backend:** FastAPI")

    st.write("**Frontend:** Streamlit")

    st.write(f"**Version:** {APP_VERSION}")

    st.write(f"**Status:** {API_STATUS}")

    st.markdown("---")

    st.info(
        "BusinessPulse-AI predicts customer churn "
        "using Machine Learning and provides "
        "business recommendations."
    )
# ============================================================
# Dashboard Header
# ============================================================

st.title(f"📊 {APP_NAME}")

st.caption(APP_SUBTITLE)

st.markdown("---")
# ============================================================
# Dashboard Metrics
# ============================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Model",
        MODEL_NAME
    )

with col2:
    st.metric(
        "Accuracy",
        MODEL_ACCURACY
    )

with col3:
    st.metric(
        "Features",
        TOTAL_FEATURES
    )

with col4:
    st.metric(
        "API",
        API_STATUS
    )

st.markdown("---")
# ============================================================
# Customer Input Form
# ============================================================

payload = customer_form()

# ============================================================
# Prediction Button
# ============================================================

predict = st.button(
    "🔍 Predict Customer Churn",
    use_container_width=True,
    type="primary"
)

# ============================================================
# Prediction
# ============================================================

if predict:

    with st.spinner("🔄 Predicting customer churn..."):

        result = predict_customer(payload)

    if result:

        display_results(result)

    else:

        st.error("Unable to connect to the prediction API.")
# ============================================================
# Footer
# ============================================================

st.markdown("---")

st.caption(
    "BusinessPulse-AI • Machine Learning • FastAPI • Streamlit • Version 1.0"
)