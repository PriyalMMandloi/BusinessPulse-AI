"""
============================================================
BusinessPulse-AI
FastAPI Client
============================================================
"""

import requests

from config import API_URL


def predict_customer(payload):
    """
    Send customer data to the FastAPI backend and
    return the prediction response.
    """

    try:

        response = requests.post(
            API_URL,
            json=payload,
            timeout=10
        )

        if response.status_code == 200:
            return response.json()

        return None

    except requests.exceptions.RequestException:

        return None