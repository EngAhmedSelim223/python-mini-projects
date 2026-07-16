todos = []

while True:
    user_action = input("Type add, show or exit: ")
    
    match user_action:
        case "add":
            todo = input("Enter a todo: ").strip().lower()
            todos.append(todo)
            
        
        case "show":
            for index, item in enumerate(todos):
                print(f"{index + 1} - {item}")
        case "exit":
            break
        case _:
            print("Please Enter a valid option add, show or exit")

print("Thanks for using our task manager app :)")
