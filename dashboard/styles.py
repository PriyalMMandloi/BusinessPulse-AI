"""
============================================================
BusinessPulse-AI
Custom Styles
============================================================
"""

import streamlit as st


def load_css():

    st.markdown(
        """
        <style>

        /* Main Content */
        .block-container{
            padding-top:2rem;
            padding-bottom:2rem;
        }

        /* Buttons */
        .stButton > button{
            width:100%;
            border-radius:10px;
            height:3.2rem;
            font-size:18px;
            font-weight:600;
        }

        /* Metrics */
        div[data-testid="metric-container"]{
            border:1px solid rgba(120,120,120,.2);
            border-radius:12px;
            padding:18px;
            box-shadow:0 2px 10px rgba(0,0,0,.05);
        }

        /* Progress */
        div[data-testid="stProgress"]{
            margin-top:12px;
            margin-bottom:12px;
        }

        /* Sidebar */
        section[data-testid="stSidebar"]{
            border-right:1px solid rgba(120,120,120,.15);
        }

        /* Inputs */
        .stSelectbox,
        .stNumberInput,
        .stSlider{
            margin-bottom:10px;
        }

        </style>
        """,
        unsafe_allow_html=True
    )