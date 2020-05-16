import random

secrect_num = random.randint(1,20)
guess_counter = 10
for i in range(1,10):
    user_guess = int(input("Guess number from 0 to 20: "))
   
    if user_guess == secrect_num:
        print("Hurray,You won !!!")
        break
    elif user_guess > secrect_num :
        guess_counter -= 1
        print("Sorry your guess was wrong")
        print("Your guess is too high try going lower")
        print(f"You have {guess_counter} guesses remaining")
    elif user_guess < secrect_num:
        guess_counter -= 1
        print("Sorry your guess was wrong")
        print("Your guess is too low try going higher")
        print(f"You have {guess_counter} guesses remaining")