import streamlit as st
import functions as funcs

def add_todo():   
    new_todo = st.session_state['new_todo'].strip() # str strip head & tail
                                                    # st.checkbox strip body & tail
    if new_todo != '':
        new_todo = new_todo + '\n'
        if not new_todo in todo_list:
            todo_list.append(new_todo)
            funcs.update_file(todo_list)
            st.session_state['new_todo'] = ''            
        else:
            st.warning(f'Dupplicate To-do. (Hint: More specific, \
                       like: "{new_todo} at 6AM")')

st.title('My To-do App')

st.subheader('This is my todo app.')

st.write('This app is to increase your productivity.')

todo_list = funcs.get_todo()

for idx, todo in enumerate(todo_list):
    chbk_key = f'{idx}. {todo}'
    chbk_ticked = st.checkbox(todo, key=chbk_key)
    if chbk_ticked:
        todo_list.pop(idx)
        funcs.update_file(todo_list)
        del st.session_state[chbk_key]
        st.experimental_rerun()

st.text_input('Enter a todo:', placeholder='Add a new to do...', on_change=add_todo,
              key='new_todo', label_visibility='collapsed')
