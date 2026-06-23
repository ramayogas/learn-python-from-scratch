import random

# def play_again():
#         restart = input("play again? (y/n): ")
#         if restart =="y":
#             game()
#         else:
#             print("Thanks for playing")

def game():
    print("guess a number between 1 and 5")
    ran=random.randint(1,5)
    
    try:
        user_input=int(input("enter your number: "))
    except ValueError: 
        print('not a number')
        return

    if user_input == ran:
            print("you win") 
    else:    
        print("you lose")   
        print("your number is", user_input, "and the number is", ran) 
game()
while True:
    restart = input("play again? (y/n): ")
    
    if restart == "y":
        game()
    else:
        print("thank you")
        break
