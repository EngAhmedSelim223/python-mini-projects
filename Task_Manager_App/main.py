todos = []

while True:
    user_action = input("Type add, show, edit or exit: ").strip().lower()
    
    match user_action:
        case "add":
            todo = input("Enter a todo: ").strip().lower()
            todos.append(todo)
            
        
        case "show":
            for index, item in enumerate(todos):
                print(f"{index + 1} - {item}")
                
        case "edit":
            todo_to_edit = int(input("Enter Todo number to edit: "))
            if todo_to_edit <= len(todos):
                new_todo = input("Enter the new todo: ")
                todos[todo_to_edit - 1] = new_todo
            else:
                print("Please Enter a valid todo number...")
        case "exit":
            break
        case _:
            print("Please Enter a valid option add, show or exit")

print("Thanks for using our task manager app :)")
