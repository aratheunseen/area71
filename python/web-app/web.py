import streamlit as st
from controllers import get_todos, set_todos

todos = get_todos('todos.txt')

st.title('YourNote')
st.write('Welcome to YourNote, a simple note taking app.')

for i, todo in enumerate(todos):
    st.checkbox(todo, key=i)


new_todo = st.text_input("", placeholder="Add a new todo here...")
# todos.append(new_todo + '\n')
# set_todos('todos.txt', todos)

print(new_todo)
