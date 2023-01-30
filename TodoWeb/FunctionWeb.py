from typing import List

FILEPATH = "todoWeb.txt"



def get_todos(filePath = FILEPATH):
    with open(filePath, 'r') as file:
        todos: list[str] = file.readlines()
        return todos


get_todos()


def write_todos(todos,filePath =FILEPATH):
    with open(filePath, 'w') as file:
        file.writelines(todos)
    return None