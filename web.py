import streamlit as st
from modules import functions

todos = functions.get_todos()


def add_todo():
    item = st.session_state["new_todo"] + "\n"
    todos.append(item)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is a demo app.")
st.write("This app is to increase the productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        st.experimental_rerun()


st.text_input(label="", placeholder="Add a new todo...",
              on_change=add_todo, key='new_todo')
