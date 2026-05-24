import random 
num=random.randint(1,10)
while True:
    guess=int(input("Guess number between 1 to 10:"))
    if guess ==0:
        print("zero is not valid guess")
        break
    elif guess>num:
        print("your guess is too high.")
    elif guess<num:
        print("you guessed too low..")
    else: 
        print("correct !!")
        break
