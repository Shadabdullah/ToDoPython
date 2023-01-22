
todo = []

while True:
    user_input = input("Enter add or Show: ")

    match user_input:
        case "add":
            tod = input("Enter a Todo: ")
            todo.append(tod)
        case "show":
            print(todo)

