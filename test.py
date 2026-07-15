tasks = []

while True:
    print("Menu: \n1. Add Task \n2. See Task and Status \n3. Edit Status \n4. Delete Task \n5. Print Tasks \n6. Exit",)
    choice = input("Choose menu: ")
    
    if choice == "1":
        new_task = input("Enter a new task: ")
        tasks.append(
            {   
                "id": len(tasks) + 1,
                "task": new_task,
                "status": None,
            }
        )
        
    elif choice == "2":
        for task in tasks:
            print(task["id"],"-", task["task"], "-", "Status: " ,task["status"])
            
    elif choice == "3":
        for task in tasks:
            print(task["id"],"-", task["task"], "-", "Status: " ,task["status"])
        task_id = input("Enter the task ID to edit: ")
        
        for task in tasks:
            if task["id"] == int(task_id):
                new_status = input("Add new status: ")
                task["status"] = new_status
            continue
        
    elif choice == "4":
        for task in tasks:
            print(task["id"],"-", task["task"], "-", "Status: " ,task["status"])
        task_id = input("Enter the task ID to delete: ")
        
        for i,task in enumerate(tasks):
            if task["id"] == int (task_id):
                print(task["id"],"-", task["task"], "sucessfully deleted")
                del tasks[i]
            continue
        
    elif choice == "5":        
        
        for i,task in enumerate(tasks):
            x = task["title"] - "Status: ", task["status"]
            print(x)
        
        with open("task_list.txt", "w") as file:
            file.write(x)
            print("task list saved to task_list.txt")
        
        with open("task_list.txt","r") as file:
            print(file.read())  
        
    elif choice == "6":
        print("Thank you")
        break