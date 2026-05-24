# Welcome to snake,water,gun game
import random
computer_choice=random.randint(1,3)
print("===== Rules =====")
print(" 1 = Snake")
print(" 2 = Water")
print(" 3 = Gun")
print("===== Rules =====")
while True:
    choice=int(input("Enter your choice:"))
    print(f"Computer's choice is :{computer_choice}")
    if choice ==1 and computer_choice==1:
        print("Its Draw cause both choice is same")
    elif choice == 2 and computer_choice == 2:
        print("Its Draw cause both choice is same")
    elif choice == 3 and computer_choice == 3:
        print("Its Draw cause both choice is same")
    elif choice == 1 and computer_choice == 2:
        print("You Lose cause Snake Drinks Water..")
    elif choice == 2 and computer_choice == 1:
        print("You won cause Snake Drinks Water..")
    elif choice == 3 and computer_choice == 2:
        print("You Lose cause Water Douses The Gun..")
    elif choice == 2 and computer_choice == 3:
        print("You Won cause Water Douses The Gun..")
    elif choice == 3 and computer_choice == 1:
        print("You won cause Gun Punishes The Snake..")
    elif choice == 1 and computer_choice == 3:
        print("You lose cause Gun Punishes The Snake..")
    txt=input("do you want to continue Y or N:")
    if txt=="Y" or txt=="y":
        print("Then play the game..")
    elif txt=="N" or txt=="n":
        break
    else:
        print("Invalid choice enter appropriate answer..")