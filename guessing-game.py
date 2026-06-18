import random
# print(random.randrange(1, 11))
# print(random.randint(1,11))

def play_again():
        restart = input("play again? (y/n): ")
        if restart =="y":
            game()
        else:
            print("Thanks for playing")

def game():
    print("guess a number between 1 and 5")
    ran=random.randint(1,5)
    while True:
        try:
            user_input = int(input())
            game()
        except ValueError:
            print("bukan int")

    if user_input == ran:
        print("you win") 
    else:    
        print("you lose")   
        print("your number is", user_input, "and the number is", rangit)
    play_again()
    
game()
    
