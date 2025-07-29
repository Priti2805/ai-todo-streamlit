# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29 15:22:43 2025

@author: user
"""

import streamlit as st
import requests

# Set page title and layout
st.set_page_config(page_title="AI Todo App", layout="centered")

# ----- CUSTOM STYLING -----
# Adds a gradient background and styled components using raw HTML/CSS
st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        background-attachment: fixed;
    }
    .block-container {
        background-color: rgba(255, 255, 255, 0.95) !important;
        padding: 2rem 2rem;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0);
    }
    button[kind="primary"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.5rem 1.5rem !important;
    }
    </style>
""", unsafe_allow_html=True)

# ----- TITLE AND DESCRIPTION -----
st.markdown("## 📝 AI Todo App")
st.markdown("Your intelligent task manager with AI-powered translation 🌍")

# ----- LANGUAGE CODES FOR TRANSLATION -----
lang_map = {
    'Spanish': 'es', 'French': 'fr', 'German': 'de', 'Italian': 'it',
    'Portuguese': 'pt', 'Chinese': 'zh', 'Japanese': 'ja', 'Korean': 'ko',
    'Arabic': 'ar', 'Hindi': 'hi', 'Russian': 'ru'
}

# ----- INITIALIZE TASK STORAGE -----
# Store task list in Streamlit's session state so it persists during interactions
if 'todos' not in st.session_state:
    st.session_state.todos = []

# ----- FORM TO ADD NEW TASK -----
with st.form("new_task_form"):
    new_task = st.text_input("➕ Add a new task")
    submitted = st.form_submit_button("Add")
    if submitted:
        if new_task.strip():
            st.session_state.todos.append({
                'text': new_task.strip(),
                'completed': False,
                'translation': ''
            })
        else:
            st.warning("Enter a task!")

# ----- LANGUAGE SELECTOR -----
target_lang = st.selectbox("🌍 Translate to", [""] + list(lang_map.keys()))

# ----- TRANSLATE ALL BUTTON -----
if st.button("🔄 Translate All"):
    if not target_lang:
        st.warning("Choose a language first.")
    else:
        for idx, todo in enumerate(st.session_state.todos):
            if todo['text'] and not todo['translation']:
                try:
                    res = requests.get("https://api.mymemory.translated.net/get", params={
                        'q': todo['text'],
                        'langpair': f'en|{lang_map[target_lang]}'
                    })
                    translated = res.json()['responseData']['translatedText']
                    st.session_state.todos[idx]['translation'] = translated
                except:
                    st.error(f"Failed to translate: {todo['text']}")

# ----- TASK STATS -----
total = len(st.session_state.todos)
completed = sum(1 for t in st.session_state.todos if t['completed'])
pending = total - completed

# Display task statistics in boxes
st.markdown("### 📊 Task Stats:")
st.markdown(f"""
<div style='display: flex; gap: 1rem;'>
    <div style='padding: 1rem; background: #e6e6ff; border-radius: 10px; flex: 1; text-align: center;'>
        ✅ <b>{completed}</b><br><small>Completed</small>
    </div>
    <div style='padding: 1rem; background: #fff3cd; border-radius: 10px; flex: 1; text-align: center;'>
        ⏳ <b>{pending}</b><br><small>Pending</small>
    </div>
    <div style='padding: 1rem; background: #d1ecf1; border-radius: 10px; flex: 1; text-align: center;'>
        📌 <b>{total}</b><br><small>Total</small>
    </div>
</div>
""", unsafe_allow_html=True)

# ----- DISPLAY TODO LIST -----
st.write("### 📋 Your Todos")
for idx, todo in enumerate(st.session_state.todos):
    cols = st.columns([0.5, 3, 1.2, 2.3])

    # Checkbox to mark complete
    with cols[0]:
        st.session_state.todos[idx]['completed'] = st.checkbox("", value=todo['completed'], key=f"cb_{idx}")

    # Display task text (strikethrough if completed)
    with cols[1]:
        task_text = f"~~{todo['text']}~~" if todo['completed'] else todo['text']
        st.markdown(f"📝 {task_text}")

    # Button to translate individual task
    with cols[2]:
        if st.button("🌐 Translate", key=f"tr_{idx}"):
            if not target_lang:
                st.warning("Choose a language.")
            else:
                try:
                    res = requests.get("https://api.mymemory.translated.net/get", params={
                        'q': todo['text'],
                        'langpair': f'en|{lang_map[target_lang]}'
                    })
                    translated = res.json()['responseData']['translatedText']
                    st.session_state.todos[idx]['translation'] = translated
                except:
                    st.error("Translation failed. Try again.")

    # Display translation (if available)
    with cols[3]:
        if todo['translation']:
            st.markdown(f"🗣️ _{todo['translation']}_")

# ----- FOOTER -----
st.caption("✨ Built with Streamlit and MyMemory Translation API")
