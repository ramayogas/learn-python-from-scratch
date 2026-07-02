print("test")
arr=[]
def todo():
    while True:
        menu = ["add","list task", "delete task", "print task", "exit"]
        for i, num in enumerate(menu, start =1):
                print(f"{i}.{num}")
        menu_choose=input("choose menu number (1/2/3): ")
        print(menu_choose)

        if menu_choose == "1":
            user_input=input("insert to do here: ")
            arr.append(user_input)
        elif menu_choose == "2":
            print(arr)
        elif menu_choose == "3":
            delete_input=input("choose deleted number task here: ")
            arr.pop(int(delete_input)-1)
        elif menu_choose == "4":
            with open("task_list.txt", "w") as file:
                file.write("\n".join(arr))
                print("task list saved to task_list.txt")
        elif menu_choose == "5":
            print("thank you for using this app")
            break
        continue
todo()
