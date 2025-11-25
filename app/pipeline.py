# app/pipeline.py

from storage import load_emails, load_prompts
from llm_agent import categorize_email, extract_action_items
import json
from pathlib import Path

PROCESSED_FILE = Path("data/processed.json")


def process_inbox():
    """
    Phase 1 pipeline:
    - Load emails
    - Run categorization + action-item extraction via LLaMA 3 (Ollama)
    - Store results in data/processed.json
    """
    emails = load_emails()
    prompts = load_prompts()

    results = []

    for email in emails:
        text = email["body"]

        category_output = categorize_email(text, prompts["categorization_prompt"])
        actions_output = extract_action_items(text, prompts["action_item_prompt"])

        results.append({
            "id": email["id"],
            "sender": email["sender"],
            "subject": email["subject"],
          
            "category_raw": category_output,
            "actions_raw": actions_output,
        })

    PROCESSED_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(PROCESSED_FILE, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    return results
