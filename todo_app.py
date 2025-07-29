# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29 12:25:15 2025

@author: user
"""

# # todo_app.py

# import streamlit as st
# import requests

# st.set_page_config(page_title="AI Todo App", layout="centered")
# st.title("📝 AI Todo App with Translation")

# # Initialize session state for todos
# if 'todos' not in st.session_state:
#     st.session_state.todos = []

# # Language code map
# lang_map = {
#     'Spanish': 'es', 'French': 'fr', 'German': 'de', 'Italian': 'it',
#     'Portuguese': 'pt', 'Chinese': 'zh', 'Japanese': 'ja', 'Korean': 'ko',
#     'Arabic': 'ar', 'Hindi': 'hi', 'Russian': 'ru'
# }

# # Input section
# new_todo = st.text_input("🆕 Add a new task")

# if st.button("➕ Add Todo"):
#     if new_todo.strip():
#         st.session_state.todos.append({
#             'text': new_todo.strip(),
#             'completed': False,
#             'translation': ''
#         })
#     else:
#         st.warning("Please enter a task!")

# # Language selection
# target_language = st.selectbox("🌍 Choose translation language", [""] + list(lang_map.keys()))

# # Show all todos
# st.subheader("📋 Todo List")
# for idx, todo in enumerate(st.session_state.todos):
#     cols = st.columns([0.5, 4, 1, 2])
    
#     with cols[0]:
#         st.session_state.todos[idx]['completed'] = st.checkbox("", value=todo['completed'], key=f"cb_{idx}")
        
#     with cols[1]:
#         st.markdown(f"{'✅ ' if todo['completed'] else '🔲 '}{todo['text']}")
    
#     with cols[2]:
#         if st.button("🌐", key=f"trans_{idx}"):
#             if not target_language:
#                 st.warning("Choose a language first.")
#             else:
#                 # Call free translation API
#                 try:
#                     r = requests.get("https://api.mymemory.translated.net/get", params={
#                         'q': todo['text'],
#                         'langpair': f'en|{lang_map[target_language]}'
#                     })
#                     translated = r.json()['responseData']['translatedText']
#                     st.session_state.todos[idx]['translation'] = translated
#                 except:
#                     st.error("Translation failed.")

#     with cols[3]:
#         if todo['translation']:
#             st.markdown(f"🗣️ _{todo['translation']}_")

# # Footer
# st.markdown("---")
# st.caption("Built with ❤️ using Streamlit and MyMemory API")
# todo_app.py

# import streamlit as st
# import requests

# st.set_page_config(page_title="AI Todo App", layout="centered")
# st.title("📝 AI Todo App with Translation")

# # Language codes for MyMemory API
# lang_map = {
#     'Spanish': 'es', 'French': 'fr', 'German': 'de', 'Italian': 'it',
#     'Portuguese': 'pt', 'Chinese': 'zh', 'Japanese': 'ja', 'Korean': 'ko',
#     'Arabic': 'ar', 'Hindi': 'hi', 'Russian': 'ru'
# }

# # Initialize todo list
# if 'todos' not in st.session_state:
#     st.session_state.todos = []

# # New todo input
# new_task = st.text_input("Add a new task")

# if st.button("➕ Add"):
#     if new_task.strip():
#         st.session_state.todos.append({
#             'text': new_task.strip(),
#             'completed': False,
#             'translation': ''
#         })
#     else:
#         st.warning("Please enter a task.")

# # Language selector
# target_lang = st.selectbox("Translate to", [""] + list(lang_map.keys()))

# # Show todos
# st.write("### 📋 Your Todo List")
# for idx, todo in enumerate(st.session_state.todos):
#     cols = st.columns([0.5, 4, 1.2, 2.3])
    
#     with cols[0]:
#         st.session_state.todos[idx]['completed'] = st.checkbox("", value=todo['completed'], key=f"cb_{idx}")
    
#     with cols[1]:
#         st.markdown(f"{'✅ ' if todo['completed'] else '🔲 '}{todo['text']}")
    
#     with cols[2]:
#         if st.button("🌐 Translate", key=f"tr_{idx}"):
#             if not target_lang:
#                 st.warning("Choose a language.")
#             else:
#                 try:
#                     r = requests.get("https://api.mymemory.translated.net/get", params={
#                         'q': todo['text'],
#                         'langpair': f'en|{lang_map[target_lang]}'
#                     })
#                     translated = r.json()['responseData']['translatedText']
#                     st.session_state.todos[idx]['translation'] = translated
#                 except:
#                     st.error("Translation failed.")

#     with cols[3]:
#         if todo['translation']:
#             st.markdown(f"🗣️ _{todo['translation']}_")

# st.caption("Built with ❤️ using Streamlit + MyMemory Translation API")
# todo_app.py

import streamlit as st
import requests

st.set_page_config(page_title="AI Todo App", layout="centered")
st.title("📝 AI Todo App")

# Language codes
lang_map = {
    'Spanish': 'es', 'French': 'fr', 'German': 'de', 'Italian': 'it',
    'Portuguese': 'pt', 'Chinese': 'zh', 'Japanese': 'ja', 'Korean': 'ko',
    'Arabic': 'ar', 'Hindi': 'hi', 'Russian': 'ru'
}

# Session state init
if 'todos' not in st.session_state:
    st.session_state.todos = []

# Add new task
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

# Language selector
target_lang = st.selectbox("🌍 Translate to", [""] + list(lang_map.keys()))

# Task counts
total = len(st.session_state.todos)
completed = sum(1 for t in st.session_state.todos if t['completed'])
pending = total - completed

st.markdown(f"""
### 📊 Task Stats:
- ✅ Completed: **{completed}**
- ⏳ Pending: **{pending}**
- 📌 Total: **{total}**
""")

# Display todos
st.write("### 📋 Your Todos")
for idx, todo in enumerate(st.session_state.todos):
    cols = st.columns([0.5, 3, 1.2, 2.3])
    
    with cols[0]:
        st.session_state.todos[idx]['completed'] = st.checkbox("", value=todo['completed'], key=f"cb_{idx}")
    
    with cols[1]:
        task_text = f"~~{todo['text']}~~" if todo['completed'] else todo['text']
        st.markdown(f"📝 {task_text}")
    
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
    
    with cols[3]:
        if todo['translation']:
            st.markdown(f"🗣️ _{todo['translation']}_")

st.caption("✨ Built with Translation API")
