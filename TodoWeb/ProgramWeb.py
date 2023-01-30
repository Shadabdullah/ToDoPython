import streamlit as st
import FunctionWeb as FB

st.title("TO DO APP")

todos = FB.get_todos()


def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    print(todos)
    FB.write_todos(todos)


# for td in todos:
#     st.checkbox(td)
for index , td in enumerate(todos):
    checkbox = st.checkbox(td ,key= td)
    if checkbox:
        todos.pop(index)
        FB.write_todos(todos)
        del st.session_state[td]

st.text_input(label='', placeholder='Enter new todos', on_change=add_todo, key='new_todo')

