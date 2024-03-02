import PySimpleGUI as sg

label1 = sg.Text('Select Files to Compress:')
input1 = sg.InputText()
button1 = sg.FilesBrowse('Browse')
label2 = sg.Text('Select Destination Folder:')
input2 = sg.InputText()
button2 = sg.FolderBrowse('Browse')

layout = [
    [label1, input1, button1],
    [label2, input2, button2],
    [sg.Button('Compress', size=(55,2), button_color=('white', 'green')), sg.Button('Exit',size=(10,2), button_color=('white', 'red'))]
]

window = sg.Window('File Compressor', layout)
window.read()
window.close()