def agecalculator():
    from datetime import date
    year = int(input("Enter your birth year: "))
    month = int(input("Enter your birth month: "))
    day = int(input("Enter your birth day: "))
    today = date.today()
    age = today.year - year - ((today.month, today.day) < (month, day))
    print("Your age is: ", age)


agecalculator()