# app/utils.py
import json
import re


def extract_json_object(text: str):
    """
    Try to extract a single JSON object from a string.
    Returns Python dict or None.
    """
    if not text:
        return None

    try:
        return json.loads(text)
    except Exception:
        pass


    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        candidate = match.group(0)
        try:
            return json.loads(candidate)
        except Exception:
            pass

    return None


def extract_json_array(text: str):
    """
    Try to extract a JSON array from a string.
    Returns Python list or [].
    """
    if not text:
        return []

    try:
        data = json.loads(text)
        if isinstance(data, list):
            return data
    except Exception:
        pass


    match = re.search(r"\[.*\]", text, re.DOTALL)
    if match:
        candidate = match.group(0)
        try:
            data = json.loads(candidate)
            if isinstance(data, list):
                return data
        except Exception:
            pass

    return []
