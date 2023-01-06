import streamlit as st
from modules import functions

todos = functions.get_todos()

# st.set_page_config(layout="wide")


def add_todo():
    item = st.session_state["new_todo"] + "\n"
    todos.append(item)
    functions.write_todos(todos)


st.title("The Todo-List App")
st.subheader("This app is to increase the productivity.")
st.write("Create new todos, edit the existing ones and mark complete once the todo is completed.")

st.text_input(label="", placeholder="Add a new todo...",
              on_change=add_todo, key='new_todo')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        st.experimental_rerun()
