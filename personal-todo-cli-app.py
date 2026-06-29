print("test")
arr=[]
def todo():
    while True:
        

        menu = ["add","list task", "delete task"]
        for i, num in enumerate(menu, start =1):
                print(f"{i}.{num}")
        menu_choose=input("choose menu number (1/2/3): ")
        print(menu_choose)

        if menu_choose == "1":
            user_input=input("insert to do here: ")
            arr.append(user_input)
        elif menu_choose == "2":
            print(arr)

        continue
todo()
