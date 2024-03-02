import features
import PySimpleGUI as sg

# Define the window layout
title = 'YourNote'
label = sg.Text('Type a todo:')
input = sg.InputText(tooltip='Type a todo', )
add_button = sg.Button('Add')
clear_button = sg.Button('Clear')
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit', size=(45, 1))

values = features.get_todos('todos.txt')
listbox = sg.Listbox(values, size=(50, 6))

layout = [
    [label],
    [input, add_button],
    [edit_button, complete_button],
    [listbox],
    [exit_button]
]

window = sg.Window(title, layout)
window.read()
window.close()

