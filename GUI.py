import Function
import PySimpleGUI as sg

label = sg.Text('Type in todo list')
input_box = sg.InputText(tooltip="Enter todo")

window = sg.Window("My To-DO App",layout=[[label],[input_box]])
window.read()

window.close()