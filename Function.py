from typing import List

FILEPATH = "todo.txt"
item = 'nice'


def get_todos():
    with open(FILEPATH, 'r') as file:
        todos: list[str] = file.readlines()
        return todos


get_todos()


def write_todos(todos):
    with open(FILEPATH , 'w') as file:
        file.writelines(todos)

    return None