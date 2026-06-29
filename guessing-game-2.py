#with level difficulties and prediction high and low
import random

def game():
    arr=[]
    ran=random.randint(1,10)
    print("choose level")
    
    while True:
        level=input("easy / hard: ")
        
        if level == "easy":
            attempts = 10
            break
        elif level == "hard":
            attempts = 3
            break
        else:
            print("please select a level")
    
    for i in range(attempts):
        try:
            user_input=int(input("guess: "))
        except ValueError:
            print("not a number")
            continue
        arr.append(user_input)
        if user_input > ran:
            print("too high")
        elif user_input < ran:
            print("too low")
        elif user_input == ran:
            print("your number is correct", ran) 
            break
            
    print("Your guesses are: "+", ".join(map(str,arr)))
    print("the number is: ",ran)
    
game()


while True:
    restart = input("play again? (y/n): ")
    
    if restart == "y":
        game()
    else:
        print("thank you")
        break
