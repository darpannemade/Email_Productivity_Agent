# app/llm_agent.py

import os
import requests


OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
MODEL_NAME = os.getenv("OLLAMA_MODEL", "llama3")


def _call_ollama(prompt: str) -> str:
    """
    Call local LLaMA 3 via Ollama's /api/generate endpoint.
    """
    url = f"{OLLAMA_BASE_URL}/api/generate"
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    try:
        resp = requests.post(url, json=payload, timeout=120)
        resp.raise_for_status()
        data = resp.json()
        return data.get("response", "").strip()
    except Exception as e:
        
        return f"[LLM ERROR] {e}"


def run_llm(system_prompt: str, user_instruction: str) -> str:
    """
    Generic wrapper to combine a 'prompt template' and user instruction.
    """
    full_prompt = f"{system_prompt}\n\nUser request:\n{user_instruction}"
    return _call_ollama(full_prompt)




def categorize_email(email_text: str, categorization_prompt: str) -> str:
    """
    Uses the categorization prompt to classify the email.
    Expected (by prompt design) to return JSON like:
    {"category": "Important"}
    """
    user_instruction = f"Categorize this email:\n\n{email_text}"
    return run_llm(categorization_prompt, user_instruction)


def extract_action_items(email_text: str, action_prompt: str) -> str:
    """
    Uses the action item prompt to extract tasks.
    Expected (by prompt design) to return JSON list.
    """
    user_instruction = f"Extract action items from this email:\n\n{email_text}"
    return run_llm(action_prompt, user_instruction)


def draft_reply(email_text: str, auto_reply_prompt: str, tone: str = "professional") -> str:
    """
    Drafts a reply using auto-reply prompt and desired tone.
    """
    user_instruction = (
        f"Draft a reply in a {tone} tone based on this email.\n\n"
        f"Email:\n{email_text}"
    )
    return run_llm(auto_reply_prompt, user_instruction)


def summarize_email(email_text: str, summary_prompt: str) -> str:
    """
    Summarizes an email using the summarization prompt.
    """
    user_instruction = f"Summarize this email briefly:\n\n{email_text}"
    return run_llm(summary_prompt, user_instruction)


def chat_with_email(email_text: str, custom_prompt: str, user_query: str) -> str:
    """
    For chat-style interaction with a selected email.
    """
    combined_prompt = (
        f"{custom_prompt}\n\n"
        f"Here is the email content:\n{email_text}\n\n"
        f"Now answer the user's question about this email."
    )
    return run_llm(combined_prompt, user_query)
