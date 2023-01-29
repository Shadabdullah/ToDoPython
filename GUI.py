import Function
import PySimpleGUI as sg

label = sg.Text('Type in todo list',font=('monospace',13))
input_box = sg.InputText(tooltip="Enter todo" ,key="todo" ,font=('Halvatica',13))
button1 = sg.Button("ADD",font=('Halvatica',13))

todos_list = sg.Listbox(values=Function.get_todos() ,key="todos" ,enable_events=True, size=[55,8])
list_edit = sg.Button("Edit")

window = sg.Window("My To-DO App",layout=[[label],[input_box ,button1] , [todos_list , list_edit]])



while True :
    event, values = window.read()
    print(event)
    print(values)
    match event :
        case  "ADD":
            values = values["todo"] + '\n'
            todos = Function.get_todos()
            todos.append(values)
            addTodos = Function.write_todos(todos)
            Function.get_todos()

        case" Edit":
            todo_to_edit = values["todos"][0]
            print(todo_to_edit)
        case sg.WINDOW_CLOSED:
            break



window.close()