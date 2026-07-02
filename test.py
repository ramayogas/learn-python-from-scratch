tasks = []

while True:
    print("Menu: 1. add task 2.See Task 3. edit status 4. delete task 5. print tasks 6. exit")
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
        print("Current tasks: \n", tasks)
    elif choice == "3":
        print("Current tasks: ", tasks )
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