import random

def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess != random_number:
        guess=int(input(f"Guess a number between 1 and {x}:- "))
        if guess<random_number:
            print("sorry , try again. You are guess a low number !!")
        elif guess>random_number:
            print("sorry,try agian . you are guess a high number !!")


    print(f"you are amazing!! you have guessed the number{random_number}.corrcetly...")

guess(10)