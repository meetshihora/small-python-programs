import random

while True:
    choice = input("Do you want to roll the dice? (y/n): ").lower()
    if choice == "y":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f'({dice1}, {dice2})')
    elif choice == "n":
        print("Bye! Thank you for playing!")
        break
    else:
        print("Invalid input")
