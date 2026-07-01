"""
============================================================
BusinessPulse-AI
Prediction Results UI
============================================================
"""

import streamlit as st


def display_results(result):

    prediction = result["Prediction"]
    probability = result["Churn Probability"]

    st.markdown("---")
    st.header("📊 Prediction Summary")

    # ========================================================
    # Summary Cards
    # ========================================================

    col1, col2 = st.columns(2)

    with col1:

        if prediction == "Yes":
            st.error("🚨 Customer is Likely to Churn")
        else:
            st.success("✅ Customer is Likely to Stay")

    with col2:

        st.metric(
            label="Churn Probability",
            value=f"{probability*100:.2f}%"
        )

    st.progress(float(probability))

    st.markdown("")

    # ========================================================
    # Risk Analysis
    # ========================================================

    if probability >= 0.70:

        st.error(
            "🔴 **Risk Level:** High Risk\n\n"
            "Immediate customer retention action is recommended."
        )

    elif probability >= 0.40:

        st.warning(
            "🟡 **Risk Level:** Medium Risk\n\n"
            "Customer should be monitored closely."
        )

    else:

        st.success(
            "🟢 **Risk Level:** Low Risk\n\n"
            "Customer appears loyal."
        )

    # ========================================================
    # Business Recommendation
    # ========================================================

    st.subheader("💡 Business Recommendation")

    if prediction == "Yes":

        st.info("""
### Suggested Actions

- 🎁 Offer a retention discount
- 📞 Contact the customer
- 📅 Recommend a long-term contract
- ⭐ Provide loyalty rewards
""")

    else:

        st.info("""
### Suggested Actions

- 😊 Continue current service
- 🎁 Reward customer loyalty
- 📧 Send appreciation offers
- 📈 Maintain customer engagement
""")