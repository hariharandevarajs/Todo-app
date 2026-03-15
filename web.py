'''
install streamlit package from python packages
'''


import streamlit as st
import functions

todos=functions.get_todos()

def add_todo():
    todo=st.session_state["new_todo"]
    print(todo)
    todos.append('\n'+todo)
    functions.write_todos(todos)


st.title("My Todo App")
#  to excute - streamlit run web.py
st.subheader("this is today todo list")
st.write("this app help to keep your work productive")
# st.checkbox("Apply oil on the head")
# st.checkbox("Learn PY ")
for todo in todos:
    todo = st.checkbox(todo)


st.text_input(label="",
              placeholder="Add New Todo Here",
              on_change=add_todo, key="new_todo")


st.session_state
