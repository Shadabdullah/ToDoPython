import Function
import time

now: str = time.strftime('%b.%d .%y .%H :%M%S')

while True:
    user_input = input("Type add | Show | edit | complete | exit : ")

    if user_input.startswith("add"):
        todo = user_input[4:] + '\n'
        todos = Function.get_todos()
        todos.append(todo)
        addTodos = Function.write_todos(todos)
    elif user_input.startswith("show"):
        todoList = Function.get_todos()
        for index, item in enumerate(todoList):
            item = item.strip('\n')
            print(index, item)

    elif user_input.startswith("edit"):
        pass
    elif user_input.startswith("complete"):
        pass
    elif user_input.startswith("exit"):
        break
    else:
        print("Invalid command")
