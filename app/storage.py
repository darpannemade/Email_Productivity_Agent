# app/storage.py
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

EMAILS_FILE = DATA_DIR / "emails.json"
PROMPTS_FILE = DATA_DIR / "prompts.json"
DRAFTS_FILE = DATA_DIR / "drafts.json"
PROCESSED_FILE = DATA_DIR / "processed.json"


def load_emails():
    with open(EMAILS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def load_prompts():
    with open(PROMPTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_prompts(prompts: dict):
    with open(PROMPTS_FILE, "w", encoding="utf-8") as f:
        json.dump(prompts, f, indent=2, ensure_ascii=False)


def load_drafts():
    if not DRAFTS_FILE.exists():
        return []
    with open(DRAFTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_drafts(drafts: list):
    with open(DRAFTS_FILE, "w", encoding="utf-8") as f:
        json.dump(drafts, f, indent=2, ensure_ascii=False)


def load_processed():
    if not PROCESSED_FILE.exists():
        return []
    with open(PROCESSED_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
