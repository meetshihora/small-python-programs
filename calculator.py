FirstAmount = int(input("Enter your frist amount: "))

Oprators = input("Enter +, -, *, / anyone oprater: ")

SecondAmount = int(input("Enter your second amount: "))

if Oprators == "+":
    print(FirstAmount, "+", SecondAmount, "=", (FirstAmount + SecondAmount))
elif Oprators == "-":
    print(FirstAmount, "-", SecondAmount, "=", (FirstAmount - SecondAmount))
elif Oprators == "*":
    print(FirstAmount, "*", SecondAmount, "=", (FirstAmount * SecondAmount))
elif Oprators == "/":
    print(FirstAmount, "/", SecondAmount, "=", (FirstAmount / SecondAmount))
else:
    print("Invalid Oprators")