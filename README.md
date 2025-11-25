📨 Email Productivity Agent (Ollama + Streamlit + n8n)

A fully local, privacy-focused AI Email Productivity Assistant powered by:

  -LLaMA 3 (via Ollama)
  
  -Streamlit UI
  
  -n8n automation workflows
  
  -Prompt-driven categorization, task extraction, and email drafting



🌟 Features


✅ 1. Load & View Inbox

Loads a mock inbox from data/emails.json (10–20 sample emails)

Shows sender, timestamp, subject, body

Category badges (To-Do, Important, Newsletter, Spam, Uncategorized)

✅ 2. Prompt Brain (Editable Prompts)

Categorization Prompt

Action-item Extraction Prompt

Auto-reply / Drafting Prompt

Changes update live across the whole system

✅ 3. Email Processing Pipeline

Runs LLaMA 3 locally via Ollama to:

Categorize every email

Extract structured action-items as JSON

Save to processed.json

Populate dashboards / insights

✅ 4. Email Agent Chat

Ask the AI questions about:

Any specific email

Summaries

Task extraction

Suggested replies

Tone-controlled response drafting

Much like ChatGPT but local + inbox-aware

✅ 5. Reply Drafts (Save, Edit, Delete, Send)

AI-generated email drafts

Editable subject + body

Save drafts

Delete one / delete all

Send drafts to n8n webhook

✅ 6. n8n Automation Integration

Drafts can be sent to n8n for:

Sending emails

Logging tasks

Saving to Google Sheets

Slack notifications

ANY custom workflow

✅ 7. Tasks & Insights Dashboard

All extracted tasks as a Knowledge Base

High-priority tasks

Tasks grouped by email

Export to n8n

✅ 8. Global Inbox Agent (RAG-lite)

Chat over your entire inbox summary:

“What are my urgent tasks?”

“Summarize HR emails from this week.”

“What should I do next?”


🗂️ Folder Structure


```
Email_Productivity_Agent/
│
├── app/
│   ├── ui.py
│   ├── llm_agent.py
│   ├── pipeline.py
│   ├── storage.py
│   ├── utils.py
│   ├── n8n_client.py
│
├── data/
│   ├── emails.json
│   ├── prompts.json
│   ├── drafts.json
│   ├── processed.json
│
├── README.md
├── requirements.txt

```



🔧 Setup Instructions

1️⃣ Install Python dependencies
pip install -r requirements.txt

2️⃣ Install Ollama (Required)

Download from:
https://ollama.ai

Then pull LLaMA model:

ollama pull llama3


Start Ollama:

ollama serve

3️⃣ Start n8n (Optional but recommended)

You can run:

n8n start


Then create a simple webhook workflow with:

Webhook Trigger

Gmail Node or Logger Node

Copy the webhook URL into n8n_client.py.

▶️ Run the Application
streamlit run app/ui.py


Streamlit will open in your browser automatically.

📥 Loading the Mock Inbox

The inbox is stored in:

data/emails.json


Format:


```json
[
  {
    "id": 1,
    "sender": "manager@company.com",
    "subject": "Project status update required",
    "timestamp": "2025-11-15 09:10:00",
    "body": "Hi... can you send the project status by Friday?"
  }
]
```



To add more:
– Copy an existing entry
– Change id, sender, subject, etc.
– Save file

The app reloads automatically.



🧠 Configuring Prompts (Prompt Brain)


Navigate to:

Sidebar → 🧠 Prompt Brain

You can edit 3 prompts:

Categorization Prompt

Action-item Extraction Prompt

Auto-Reply Prompt

Prompts are saved to:

data/prompts.json


Changing prompts will immediately alter:

Categorization

Extracted tasks

AI replies

Drafts

Global inbox agent behavior


⚙️ Usage Flow (Example)

1️⃣ Go to Inbox

View all mock emails & category badges.

2️⃣ Open Prompt Brain

Modify categorization / task extraction prompts.

3️⃣ Process Inbox

Runs entire pipeline:

Categorization
Task extraction
Metadata generation
Saving to processed.json

4️⃣ Chat with email

Ask:

“Summarize this email”

“Extract the tasks”

“Create a professional reply”

“Rewrite this politely”

5️⃣ Reply Drafts

Generate AI draft

Edit subject/body

Save

Delete

Send via n8n

6️⃣ Tasks & Insights

Shows all tasks extracted across inbox:

Total tasks

High priority

Urgent items

Task list per email

Export to n8n

7️⃣ Global Inbox Agent

Ask questions like:

“What are my urgent tasks today?”

“Which emails are marked To-Do?”

“Give me a weekly summary.”


📂 Assets Included

1️⃣ Mock Inbox (20 sample emails)

→ data/emails.json
Generated specifically for enterprise + personal scenarios:

HR

Managers

Meetings

Spam

Newsletters

Task-heavy emails

Alerts

Follow-ups

2️⃣ Default Prompts

→ data/prompts.json
Carefully tuned for:

Stable categorization

Strong JSON extraction

Professional reply drafting

3️⃣ Starter processed.json & drafts.json

→ safely included (empty by default)



🧱 Architecture Diagram -

```text
               ┌────────────────────┐
               │     User UI        │
               │    (Streamlit)     │
               └─────────┬──────────┘
                         │
         ┌───────────────┴────────────────────┐
         │                                    │
 ┌───────▼────────────┐             ┌─────────▼──────────┐
 │   Email Agent       │             │  Processing        │
 │ (Chat + Drafts)     │             │    Pipeline        │
 └─────────┬───────────┘             └─────────┬──────────┘
           │                                     │
   ┌───────▼──────────────┐          ┌──────────▼────────────┐
   │   LLaMA 3 (Ollama)    │          │   Storage (JSON)       │
   └─────────┬─────────────┘          └──────────┬────────────┘
             │                                     │
      ┌──────▼──────────────┐      ┌──────────────▼─────────────┐
      │   Prompt Templates   │      │      n8n Automation         │
      └──────────────────────┘      └────────────────────────────┘
```


