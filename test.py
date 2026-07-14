tasks = []

while True:
    print("Menu: \n1. add task \n2. See Task \n3. edit status \n4. delete task \n5. print tasks \n6. exit",)
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
            print(task["id"],"-", task["task"])
    elif choice == "3":
        for task in tasks:
            print(task["id"],"-", task["task"])
        task_id = input("Enter the task ID to edit: ")
        
        for task in tasks:
            if task["id"] == int(task_id):
                new_status = input("Add new status: ")
                task["status"] = new_status
            continue
        
    elif choice == "5":
        with open("task_list.txt", "w") as file:
            file.write("\n".join(tasks))
            print("task list saved to task_list.txt")