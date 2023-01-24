


while True:
    user_input = input("Enter add or Show: ")

    match user_input:
        case "add":
            tod = input("Enter a Todo: ")+"\n"
            file = open("todo.txt",'r')
            todos = file.readlines()
            file.close()

            todos.append(tod)

            file = open('todo.txt','w')
            data = file.writelines(todos)
            file.close()


        case "show":
            file = open("todo.txt",'r')
            todos = file.readlines()
            file.close()
            for ind , item in enumerate (todos):
                print(f"{ind+1} : { item}")

        case "delete" :
            pass

        case "edit" :
            pass
        case _ :
            pass
