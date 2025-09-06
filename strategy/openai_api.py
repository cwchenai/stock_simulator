"""Wrapper around the OpenAI API using dotenv for key management."""
from __future__ import annotations

import os
from typing import Any

from dotenv import load_dotenv

try:
    import openai
except Exception as exc:  # pragma: no cover - import guard
    openai = None  # type: ignore
    _import_error = exc
else:
    _import_error = None


load_dotenv()


def ask_openai(prompt: str) -> str:
    """Send ``prompt`` to OpenAI and return the response text.

    Raises:
        RuntimeError: if the OpenAI package is missing or the API key is unset.
    """

    if _import_error is not None:
        raise RuntimeError(
            "openai package is required. Install with `pip install openai`."
        ) from _import_error

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY environment variable is not set")

    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message["content"].strip()
