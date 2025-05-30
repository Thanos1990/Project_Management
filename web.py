import streamlit as st
from modules import functions


def add_todo():
    todo = st.session_state["new_todo"]  + "\n"
    todos.append(todo)
    functions.write_todos(todos)


todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

st.text_input(label="", placeholder="Add new todo.",
              on_change=add_todo, key='new_todo')

todo_index = 0
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo_index)
    todo_index+=1
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo_index]
        st.rerun()


