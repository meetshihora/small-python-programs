def converter(f):
    c =(f -32) * 5/9
    return c

f = float(input("Enter the temperature in fahrenheit: "))
c = converter(f)
print("The temperature in celsius is: ", c)
