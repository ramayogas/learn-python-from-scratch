tasks = [
    {
        "id": 1,
        "title": "Buy groceries",
        "completed": "not yet"
    },
    {
        "id": 2,
        "title": "Finish homework",
        "completed": "done"
    },
    {
        "id": 3,
        "title": "Go for a run",
        "completed": "not yet"
    }
]


# for i, task in enumerate(tasks):
#     x = print(f"{task["title"]} \nStatus: ",f"{task["completed"]}")
    

with open("task_list.txt", "w") as file:
    for i, task in enumerate(tasks):
        x = print(f"{task["title"]} \nStatus: ",f"{task["completed"]}")
        file.write(str(x))
        print("task list saved to task_list.txt")