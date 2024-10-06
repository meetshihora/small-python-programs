import random

num = random.randint(1, 100)

while True:

    try:
        guess = int(input("Enter your guss: "))

        if guess == num:
            print("Yahh!! You won")
            break
        elif guess > num:
            print("Too high")
        elif guess < num:
            print("Too low")
        else:
            print("Sorry! Invalid input")
            
    except ValueError:
        print("Sorry! Invalid input")