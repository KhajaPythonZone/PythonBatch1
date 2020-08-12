import random
lucky_number = random.randint(1,100)
while True:
    user_guess = int(input('Enter your guess : '))
    if user_guess < lucky_number:
        print("Guess higher")
    elif user_guess > lucky_number:
        print("Guess lower")
    else:
        print("congrats you were great at guessing")
        break

    accept_defeat = int(input("Enter 0 to accept defeat any other number to continue: "))
    if accept_defeat == 0:
        print(lucky_number)
        break