# app/ui.py
import streamlit as st
from storage import (
    load_emails,
    load_prompts,
    save_prompts,
    load_drafts,
    save_drafts,
    load_processed,
)
from utils import extract_json_object, extract_json_array


def setup_page():
    st.set_page_config(
        page_title="Email Productivity Agent",
        page_icon="📨",
        layout="wide",
    )

def setup_page():
    st.set_page_config(
        page_title="Email Productivity Agent",
        page_icon="📨",
        layout="wide",
    )

    # CSS
    st.markdown(
        """
        <style>

        /* --------- MAIN TITLE / SUBTITLE --------- */
        .main-title {
            font-size: 2.1rem;
            font-weight: 700;
            padding-bottom: 0.2rem;
        }
        .subtitle {
            color: #888;
            font-size: 0.95rem;
            margin-bottom: 1rem;
        }

        /* --------- METRIC CARDS --------- */
        .metric-card {
            padding: 1.2rem;
            border-radius: 12px;
            color: white;
            margin-bottom: 0.8rem;
            text-align: center;
            box-shadow: 0 4px 12px rgba(0,0,0,0.12);
        }
        .metric-blue {
            background: linear-gradient(135deg, #1e3c72, #2a5298);
        }
        .metric-purple {
            background: linear-gradient(135deg, #7b4397, #9d50bb);
        }
        .metric-green {
            background: linear-gradient(135deg, #11998e, #38ef7d);
        }
        .metric-red {
            background: linear-gradient(135deg, #cb2d3e, #ef473a);
        }
        .metric-number {
            font-size: 2rem;
            font-weight: 700;
            margin-top: 0.4rem;
        }
        .metric-label {
            font-size: 0.85rem;
            opacity: 0.9;
            letter-spacing: 0.05em;
            text-transform: uppercase;
        }

        /* --------- CATEGORY BADGES --------- */
        .category-badge {
            display: inline-block;
            padding: 0.15rem 0.5rem;
            border-radius: 999px;
            font-size: 0.75rem;
            font-weight: 600;
            color: white;
            margin-left: 0.3rem;
        }
        .category-todo    { background: #1e88e5; }
        .category-important { background: #fb8c00; }
        .category-newsletter { background: #43a047; }
        .category-spam    { background: #e53935; }
        .category-unknown { background: #757575; }

        /* --------- SIDEBAR STYLING --------- */
        [data-testid="stSidebar"] {
            background: radial-gradient(circle at top left, #1f2933, #020617);
            color: #e5e7eb;
        }

        .sidebar-header {
            padding: 1rem 0.5rem 1rem 0.5rem;
            border-bottom: 1px solid rgba(148,163,184,0.4);
            margin-bottom: 0.5rem;
        }
        .sidebar-title {
            font-size: 1.2rem;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 0.4rem;
        }
        .sidebar-badge {
            font-size: 0.7rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: #38bdf8;
            margin-top: 0.1rem;
        }
        .sidebar-caption {
            font-size: 0.8rem;
            color: #9ca3af;
            margin-top: 0.3rem;
        }

        /* Radio container & labels in sidebar */
        [data-testid="stSidebar"] .stRadio > div {
            gap: 0.15rem;
        }

        [data-testid="stSidebar"] .stRadio label {
            font-size: 0.9rem;
            color: #e5e7eb;
            padding: 0.35rem 0.75rem;
            border-radius: 999px;
            transition: background 0.2s ease, transform 0.1s ease;
        }

        [data-testid="stSidebar"] .stRadio label:hover {
            background: rgba(148,163,184,0.2);
            transform: translateX(3px);
        }

        /* Hide default radio label text (we use icons in options already) */
        [data-testid="stSidebar"] .stRadio > label {
            font-size: 0.85rem;
            color: #9ca3af;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

    # JS (sidebar header animation – may be ignored by some Streamlit versions, but safe)
    st.markdown(
        """
        <script>
        document.addEventListener('DOMContentLoaded', function() {
            try {
                const header = window.parent.document.querySelector('.sidebar-header');
                if (header) {
                    header.style.transition = 'transform 0.3s ease, opacity 0.3s ease';
                    header.style.transform = 'translateY(-8px)';
                    header.style.opacity = '0';
                    setTimeout(() => {
                        header.style.transform = 'translateY(0)';
                        header.style.opacity = '1';
                    }, 150);
                }
            } catch (e) {
                // ignore if not accessible
            }
        });
        </script>
        """,
        unsafe_allow_html=True,
    )







def render_header():
    st.markdown('<div class="main-title">📨 Email Productivity Agent</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle">AI-powered inbox assistant with LLaMA 3, task extraction, drafts, and n8n automation.</div>',
        unsafe_allow_html=True,
    )


def main():
    setup_page()
    render_header()

    with st.sidebar:
        st.markdown(
            """
            <div class="sidebar-header">
                <div class="sidebar-title">📨 Email Agent</div>
                <div class="sidebar-badge">LLaMA 3 · Ollama · n8n</div>
                <div class="sidebar-caption">
                    Navigate between inbox, prompts, processing, chat, drafts and analytics.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        page = st.radio(
            "Navigation",
            [
                "🏠 Overview",
                "📥 Inbox",
                "🧠 Prompt Brain",
                "⚙️ Process Inbox",
                "💬 Email Agent Chat",
                "✍️ Reply Drafts",
                "📊 Tasks & Insights",
                "📡 Global Inbox Agent",
            ],
            label_visibility="collapsed",
        )



    emails = load_emails()
    prompts = load_prompts()

    if page == "🏠 Overview":
        render_overview(emails)

    elif page == "📥 Inbox":
        render_inbox(emails)

    elif page == "🧠 Prompt Brain":
        render_prompt_brain(prompts)

    elif page == "⚙️ Process Inbox":
        render_process_inbox()

    elif page == "💬 Email Agent Chat":
        render_email_chat(emails)

    elif page == "✍️ Reply Drafts":
        render_reply_drafts(emails)

    elif page == "📊 Tasks & Insights":
        render_tasks_insights()
        
    elif page == "📡 Global Inbox Agent":
        render_global_inbox_agent()



# ---------------------- PAGE RENDERERS ----------------------


def render_overview(emails):
    st.markdown("### 🔍 Overview")

    total_emails = len(emails)
    unique_senders = len(set(e["sender"] for e in emails)) if emails else 0

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            f"""
            <div class="metric-card metric-blue">
                <div class="metric-label">Total Emails</div>
                <div class="metric-number">{total_emails}</div>
            </div>
            """, unsafe_allow_html=True
        )
    
    with col2:
        st.markdown(
            f"""
            <div class="metric-card metric-purple">
                <div class="metric-label">Unique Senders</div>
                <div class="metric-number">{unique_senders}</div>
            </div>
            """, unsafe_allow_html=True
        )
    
    with col3:
        st.markdown(
            f"""
            <div class="metric-card metric-green">
                <div class="metric-label">Features Enabled</div>
                <div class="metric-number">6</div>
            </div>
            """, unsafe_allow_html=True
        )


    st.write("---")
    st.markdown("#### 📌 What this app can do")
    st.markdown(
        """
        - Categorize emails and extract action items using local LLaMA 3 (Ollama)  
        - Maintain editable prompt configurations via the **Prompt Brain**  
        - Process the entire inbox into a structured knowledge base  
        - Chat with any email for summaries, clarifications, and decisions  
        - Generate, edit, and save reply drafts  
        - Export tasks and send drafts via **n8n** workflows  
        """
    )

    st.write("#### 🧩 Suggested demo flow")
    st.markdown(
        """
        1. Open **Inbox** and show mock emails  
        2. Tune behavior in **Prompt Brain**  
        3. Run **Process Inbox** and inspect processed output  
        4. Use **Email Agent Chat** on a chosen email  
        5. Generate and save a draft in **Reply Drafts**  
        6. View tasks in **Tasks & Insights** and optionally export via n8n  
        """
    )

def render_global_inbox_agent():
    st.markdown("### 📡 Global Inbox Agent — Chat Over Your Inbox")

    from storage import load_processed
    from utils import extract_json_object, extract_json_array
    from llm_agent import run_llm

    processed = load_processed()
    if not processed:
        st.warning("No processed data found. Please run 'Process Inbox' first.")
        return

    # Build a compact knowledge base string
    kb_lines = []
    for item in processed:
        email_id = item["id"]
        sender = item["sender"]
        subject = item["subject"]

        cat_obj = extract_json_object(item.get("category_raw", ""))
        category = None
        if isinstance(cat_obj, dict):
            category = cat_obj.get("category")

        kb_lines.append(
            f"Email {email_id}: from {sender}, subject '{subject}', category: {category}"
        )

        actions = extract_json_array(item.get("actions_raw", ""))
        for a in actions:
            task = a.get("task")
            deadline = a.get("deadline")
            priority = a.get("priority")
            kb_lines.append(
                f"  - Task: {task}, deadline: {deadline}, priority: {priority}"
            )

    kb_text = "\n".join(kb_lines)

    st.markdown("#### 📚 Current Inbox Knowledge Base (summary)")
    with st.expander("Show internal KB text (debug)", expanded=False):
        st.text(kb_text)

    st.markdown("#### 💬 Ask Questions About Your Inbox")
    st.write(
        "Example questions: "
        "`What are my high priority tasks?`, "
        "`Which emails are To-Do?`, "
        "`Summarize my tasks from HR emails`."
    )

    if "global_chat_history" not in st.session_state:
        st.session_state.global_chat_history = []

    # 1. Show existing messages
    for msg in st.session_state.global_chat_history:
        st.chat_message(msg["role"]).write(msg["content"])

    # 2. Take new input
    user_query = st.chat_input("Ask something about your entire inbox...")

    if user_query:
        # 2a. Save user message
        st.session_state.global_chat_history.append(
            {"role": "user", "content": user_query}
        )

        # 2b. Show user message immediately
        st.chat_message("user").write(user_query)

        # 2c. Prepare prompts
        system_prompt = (
            "You are an assistant that analyzes an inbox knowledge base. "
            "You receive a structured summary of emails, categories, and tasks, and you must "
            "answer questions about priorities, deadlines, senders, and what the user should do. "
            "Be concise, structured, and specific. If you are unsure, say so."
        )

        user_instruction = (
            f"Here is the inbox knowledge base:\n{kb_text}\n\n"
            f"User question: {user_query}"
        )

        # 2d. Assistant bubble with spinner
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = run_llm(system_prompt, user_instruction)

                st.session_state.global_chat_history.append(
                    {"role": "assistant", "content": response}
                )

                st.write(response)


    
def render_inbox(emails):
    from storage import load_processed
    from utils import extract_json_object

    st.markdown("### 📥 Inbox (Mock Data)")

    if not emails:
        st.info("No emails found in the mock inbox.")
        return

    # Build category map from processed data
    processed = load_processed()
    category_map = {}
    for item in processed:
        cat_obj = extract_json_object(item.get("category_raw", ""))
        category = None
        if isinstance(cat_obj, dict):
            category = (cat_obj.get("category") or "").strip()
        category_map[item["id"]] = category

    total_emails = len(emails)
    unique_senders = len(set(e["sender"] for e in emails))
    latest = max(e.get("timestamp", "") for e in emails)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            f"""
            <div class="metric-card metric-blue">
                <div class="metric-label">Total Emails</div>
                <div class="metric-number">{total_emails}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            f"""
            <div class="metric-card metric-purple">
                <div class="metric-label">Unique Senders</div>
                <div class="metric-number">{unique_senders}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col3:
        st.markdown(
            f"""
            <div class="metric-card metric-green">
                <div class="metric-label">Latest Timestamp</div>
                <div class="metric-number">{latest or "-"} </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("---")
    st.markdown("#### 📬 Emails")

    # Simple filter by sender
    senders = ["All"] + sorted(list(set(e["sender"] for e in emails)))
    selected_sender = st.selectbox("Filter by sender", senders)

    for email in emails:
        if selected_sender != "All" and email["sender"] != selected_sender:
            continue

        email_id = email["id"]
        category = category_map.get(email_id)

        # Decide badge class
        if not category:
            badge_class = "category-unknown"
            cat_label = "Uncategorized"
        else:
            cat_lower = category.lower()
            if "to-do" in cat_lower or "todo" in cat_lower:
                badge_class = "category-todo"
            elif "important" in cat_lower:
                badge_class = "category-important"
            elif "newsletter" in cat_lower:
                badge_class = "category-newsletter"
            elif "spam" in cat_lower:
                badge_class = "category-spam"
            else:
                badge_class = "category-unknown"
            cat_label = category

        header_html = (
            f"[{email_id}] {email['subject']} — {email['sender']}"
            f" <span class='category-badge {badge_class}'>{cat_label}</span>"
        )

        with st.expander(header_html, expanded=False):
            st.markdown(f"**From:** {email['sender']}")
            st.markdown(f"**Timestamp:** {email.get('timestamp', '-')}")
            st.markdown(f"**Category:** `{cat_label}`")
            st.markdown("**Body:**")
            st.write(email["body"])

    st.caption(
        "Note: Categories appear after running **Process Inbox**, based on the current categorization prompt."
    )




def render_prompt_brain(prompts):
    st.markdown("### 🧠 Prompt Brain (Configuration)")
    st.info("These prompts control how the Email Agent classifies, extracts tasks, and drafts replies.")

    tab1, tab2, tab3 = st.tabs(["Categorization", "Action Items", "Auto-Reply"])

    with tab1:
        cat = st.text_area(
            "Categorization Prompt",
            prompts.get("categorization_prompt", ""),
            height=200,
        )
    with tab2:
        action = st.text_area(
            "Action Item Extraction Prompt",
            prompts.get("action_item_prompt", ""),
            height=220,
        )
    with tab3:
        auto = st.text_area(
            "Auto-Reply Prompt",
            prompts.get("auto_reply_prompt", ""),
            height=220,
        )

    if st.button("💾 Save Prompts"):
        prompts["categorization_prompt"] = cat
        prompts["action_item_prompt"] = action
        prompts["auto_reply_prompt"] = auto
        save_prompts(prompts)
        st.success("Prompts saved successfully!")


def render_process_inbox():
    st.markdown("### ⚙️ Process Inbox with LLaMA 3 (Ollama)")

    st.info(
        "This step runs categorization and action-item extraction on all emails using your current prompts. "
        "Results are stored in `data/processed.json` and used by the Tasks & Insights page."
    )

    if st.button("🚀 Run Processing Pipeline"):
        from pipeline import process_inbox

        with st.spinner("Processing inbox with LLaMA 3..."):
            results = process_inbox()
        st.success("Inbox processed successfully!")
        with st.expander("View raw processed output (debug)"):
            st.json(results)


def render_email_chat(emails):
    st.markdown("### 💬 Email Agent — Chat with Your Emails")

    if not emails:
        st.info("No emails available to chat with. Please add some to the mock inbox.")
        return

    from llm_agent import chat_with_email

    # Email selection
    email_subjects = {email["subject"]: email for email in emails}
    selected_subject = st.selectbox("Select an email to chat with:", list(email_subjects.keys()))
    selected_email = email_subjects[selected_subject]
    email_id = selected_email["id"]

    # Manage per-email chat history
    if "last_selected_email_id" not in st.session_state:
        st.session_state.last_selected_email_id = email_id
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # If user changed email, reset history for the new one
    if st.session_state.last_selected_email_id != email_id:
        st.session_state.chat_history = []
        st.session_state.last_selected_email_id = email_id

    st.markdown("#### 📧 Email Content")
    st.info(selected_email["body"])

    st.write("---")
    st.markdown("#### 💬 Conversation")

    # 1. Show existing history
    for msg in st.session_state.chat_history:
        st.chat_message(msg["role"]).write(msg["content"])

    # 2. Take new user message
    user_query = st.chat_input("Ask something about this email...")

    if user_query:
        # 2a. Add user message to history
        st.session_state.chat_history.append({"role": "user", "content": user_query})

        # 2b. Show user message immediately
        st.chat_message("user").write(user_query)

        # 2c. Prepare prompt
        custom_prompt = (
            "You are an intelligent email assistant. "
            "You analyze the email and answer user questions truthfully, concisely, "
            "and in simple language that a busy professional can understand."
        )

        # 2d. Show assistant bubble with spinner while thinking
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                agent_response = chat_with_email(
                    email_text=selected_email["body"],
                    custom_prompt=custom_prompt,
                    user_query=user_query,
                )

                # Save assistant reply
                st.session_state.chat_history.append(
                    {"role": "assistant", "content": agent_response}
                )

                # Show reply
                st.write(agent_response)



def render_reply_drafts(emails):
    st.markdown("### ✍️ Reply Drafts — Generate, Edit, Save, and Send via n8n")

    if not emails:
        st.info("No emails available to draft replies for.")
        return

    from llm_agent import draft_reply
    from n8n_client import send_draft_to_n8n
    from storage import load_drafts, save_drafts
    from utils import extract_json_object

    col_left, col_right = st.columns([2, 2])

    # ---------- LEFT: Generate / Edit current draft ----------
    with col_left:
        st.markdown("#### 🧾 Generate a Reply Draft")

        email_subjects = {email["subject"]: email for email in emails}
        selected_subject = st.selectbox("Select an email:", list(email_subjects.keys()))
        selected_email = email_subjects[selected_subject]

        st.markdown("**Original Email:**")
        st.info(selected_email["body"])

        tone = st.selectbox(
            "Select reply tone:",
            ["professional", "friendly", "formal", "casual"],
            index=0,
        )

        if st.button("✨ Generate Reply Draft"):
            prompts = load_prompts()
            auto_reply_prompt = prompts.get("auto_reply_prompt", "")

            if not auto_reply_prompt:
                st.error("Auto-Reply Prompt is empty! Please configure it in the Prompt Brain section.")
            else:
                raw_reply = draft_reply(
                    email_text=selected_email["body"],
                    auto_reply_prompt=auto_reply_prompt,
                    tone=tone,
                )

                # Try to parse JSON structure (subject, body, suggested_followups, metadata)
                parsed = extract_json_object(raw_reply)

                if isinstance(parsed, dict) and ("body" in parsed or "subject" in parsed):
                    subject = parsed.get("subject") or f"Re: {selected_email['subject']}"
                    body = parsed.get("body") or raw_reply
                    suggested_followups = parsed.get("suggested_followups") or []
                    metadata = parsed.get("metadata") or {}
                else:
                    # Fallback: treat whole reply as plain body (current behaviour)
                    subject = f"Re: {selected_email['subject']}"
                    body = raw_reply
                    suggested_followups = []
                    metadata = {}

                st.session_state.current_draft = {
                    "related_email_id": selected_email["id"],
                    "to": selected_email["sender"],
                    "subject": subject,
                    "body": body,
                    "suggested_followups": suggested_followups,
                    "metadata": metadata,
                }

        if "current_draft" in st.session_state:
            st.markdown("#### ✏️ Edit Current Draft")
            current = st.session_state.current_draft
            subject = st.text_input("Subject", current["subject"])
            body = st.text_area("Body", current["body"], height=200)

            col_a, col_b = st.columns(2)
            with col_a:
                if st.button("💾 Save Draft"):
                    drafts = load_drafts()
                    drafts.append(
                        {
                            "related_email_id": current["related_email_id"],
                            "to": current["to"],
                            "subject": subject,
                            "body": body,
                            "suggested_followups": current.get("suggested_followups", []),
                            "metadata": current.get("metadata", {}),
                        }
                    )
                    save_drafts(drafts)
                    st.success("Draft saved successfully!")
            with col_b:
                if st.button("🧹 Clear Current Draft (Session)"):
                    del st.session_state.current_draft
                    st.info("Current in-memory draft cleared. Saved drafts are still preserved.")

    # ---------- RIGHT: Saved drafts + delete + send ----------
    with col_right:
        st.markdown("#### 📂 Saved Drafts")

        drafts = load_drafts()
        if not drafts:
            st.info("No drafts saved yet.")
        else:
            # --- Confirmation state for deleting ALL drafts ---
            if "confirm_delete_all_drafts" not in st.session_state:
                st.session_state.confirm_delete_all_drafts = False

            if st.session_state.confirm_delete_all_drafts:
                st.warning("Are you sure you want to delete **ALL** saved drafts? This cannot be undone.")
                c1, c2 = st.columns(2)
                with c1:
                    if st.button("✅ Yes, delete all drafts"):
                        save_drafts([])
                        st.session_state.confirm_delete_all_drafts = False
                        st.success("All saved drafts deleted.")
                        st.rerun()
                with c2:
                    if st.button("❌ Cancel"):
                        st.session_state.confirm_delete_all_drafts = False
                        st.info("Deletion cancelled.")
            else:
                if st.button("🧨 Delete ALL saved drafts"):
                    st.session_state.confirm_delete_all_drafts = True

            # --- Individual drafts list ---
            for i, d in enumerate(drafts, start=1):
                with st.expander(f"Draft {i}: {d['subject']} → {d['to']}"):
                    st.markdown(f"**To:** {d['to']}")
                    st.markdown(f"**Subject:** {d['subject']}")
                    st.markdown("**Body:**")
                    st.write(d["body"])

                    # Optional extras
                    followups = d.get("suggested_followups") or []
                    metadata = d.get("metadata") or {}

                    if followups:
                        st.markdown("**Suggested Follow-ups:**")
                        for f in followups:
                            st.markdown(f"- {f}")

                    if metadata:
                        st.markdown("**Metadata:**")
                        st.json(metadata)

                    col_x, col_y = st.columns(2)
                    with col_x:
                        if st.button(
                            f"📤 Send this draft via n8n (Demo) — Draft {i}",
                            key=f"send_draft_{i}",
                        ):
                            payload = {
                                "to": d["to"],
                                "subject": d["subject"],
                                "body": d["body"],
                                "related_email_id": d.get("related_email_id"),
                            }
                            result = send_draft_to_n8n(payload)
                            if result.get("ok"):
                                st.success(
                                    f"Draft sent to n8n successfully! (HTTP {result.get('status_code')})"
                                )
                                st.write("n8n response:")
                                st.json(result.get("data"))
                            else:
                                st.error("Failed to send draft to n8n")
                                st.write("Error detail:")
                                st.write(result.get("error"))

                    with col_y:
                        if st.button(
                            f"🗑 Delete this draft — Draft {i}",
                            key=f"delete_draft_{i}",
                        ):
                            new_drafts = [x for j, x in enumerate(drafts) if j != (i - 1)]
                            save_drafts(new_drafts)
                            st.success("Draft deleted.")
                            st.rerun()



def render_tasks_insights():
    st.markdown("### 📊 Tasks & Insights — Inbox Knowledge Base (RAG-lite)")

    processed = load_processed()
    if not processed:
        st.warning("No processed data found. Please run 'Process Inbox' first.")
        return

    tasks = []
    categorized_emails = []

    for item in processed:
        email_id = item["id"]
        sender = item["sender"]
        subject = item["subject"]

        cat_obj = extract_json_object(item.get("category_raw", ""))
        category = None
        if isinstance(cat_obj, dict):
            category = cat_obj.get("category")

        categorized_emails.append(
            {
                "id": email_id,
                "sender": sender,
                "subject": subject,
                "category": category,
            }
        )

        actions_list = extract_json_array(item.get("actions_raw", ""))
        for action in actions_list:
            tasks.append(
                {
                    "email_id": email_id,
                    "sender": sender,
                    "subject": subject,
                    "task": action.get("task"),
                    "deadline": action.get("deadline"),
                    "priority": action.get("priority"),
                }
            )

    total_tasks = len(tasks)
    high_priority = len([t for t in tasks if t.get("priority") == "High"])
    todo_emails = len([e for e in categorized_emails if e.get("category") == "To-Do"])

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            f"""
            <div class="metric-card metric-purple">
                <div class="metric-label">Total Tasks</div>
                <div class="metric-number">{total_tasks}</div>
            </div>
            """, unsafe_allow_html=True
        )
    
    with col2:
        st.markdown(
            f"""
            <div class="metric-card metric-red">
                <div class="metric-label">High Priority Tasks</div>
                <div class="metric-number">{high_priority}</div>
            </div>
            """, unsafe_allow_html=True
        )
    
    with col3:
        st.markdown(
            f"""
            <div class="metric-card metric-blue">
                <div class="metric-label">To-Do Emails</div>
                <div class="metric-number">{todo_emails}</div>
            </div>
            """, unsafe_allow_html=True
        )



    st.write("---")
    st.markdown("#### 📂 Email Categories (Knowledge Base View)")
    with st.expander("Show categorized emails"):
        st.json(categorized_emails)

    st.write("#### ✅ Extracted Tasks")
    if tasks:
        st.json(tasks)
    else:
        st.info("No action items extracted from emails.")

    st.write("#### 🚨 Urgent Tasks (High Priority)")
    urgent = [t for t in tasks if t.get("priority") == "High"]
    if urgent:
        st.json(urgent)
    else:
        st.info("No urgent tasks detected based on current rules.")

    # Optional: Integrate with n8n from here
    from n8n_client import send_tasks_to_n8n

    if tasks and st.button("📤 Export all tasks to n8n"):
        result = send_tasks_to_n8n(tasks)
        if result.get("ok"):
            st.success(f"Tasks sent to n8n successfully! (HTTP {result.get('status_code')})")
            st.write("n8n response:")
            st.json(result.get("data"))
        else:
            st.error("Failed to send tasks to n8n")
            st.write("Error detail:")
            st.write(result.get("error"))


if __name__ == "__main__":
    main()
