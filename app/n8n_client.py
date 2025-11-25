# app/n8n_client.py

import os
import requests


N8N_BASE_URL = os.getenv("N8N_BASE_URL", "http://localhost:5678")
TASKS_WEBHOOK_PATH = os.getenv("N8N_TASKS_WEBHOOK_PATH", "/webhook-test/email-agent-tasks")
DRAFT_WEBHOOK_PATH = os.getenv("N8N_DRAFT_WEBHOOK_PATH", "/webhook-test/email-agent-send-draft")


def send_tasks_to_n8n(tasks: list) -> dict:
    """
    Send extracted tasks to n8n via webhook.
    """
    url = N8N_BASE_URL + TASKS_WEBHOOK_PATH
    payload = {"tasks": tasks}

    try:
        resp = requests.post(url, json=payload, timeout=30)
        resp.raise_for_status()
        return {"ok": True, "status_code": resp.status_code, "data": resp.json()}
    except Exception as e:
        return {"ok": False, "error": str(e)}


def send_draft_to_n8n(draft: dict) -> dict:
    """
    Send a single draft email to n8n via webhook.
    """
    url = N8N_BASE_URL + DRAFT_WEBHOOK_PATH

    try:
        resp = requests.post(url, json=draft, timeout=30)
        resp.raise_for_status()
        return {"ok": True, "status_code": resp.status_code, "data": resp.json()}
    except Exception as e:
        return {"ok": False, "error": str(e)}
