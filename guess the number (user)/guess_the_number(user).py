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



def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback != 'c':
        if low !=high:
            guess=random.randint(low,high)
        else:
            guess=low
        feedback=input(f"Is {guess} too high (H), too low (L), corrcect(C) ??").lower()
        if feedback =='h':
            high=guess-1
        elif feedback =='l':
            low=guess+1
    print(f"ohho ! The computer gueesed your number {guess},correctly.")


computer_guess(1000)